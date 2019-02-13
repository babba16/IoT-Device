# prompt user to feed the dog @ 8am, 12pm, 8pm
from messageDecoder import *
from dispensing import *
import time

#maxDayLimit = 3

# function to check set feeding times
def feeding_time(settings, foodInDay, foodatprevstart):
	current_time = time.strftime("%H:%M:%S")
	# prompt user to feed dog at 8am, 12pm, 8pm
	if current_time != "15:31:00":
		foodEaten = 1 - bowlFood(settings)
		foodatstart = bowlFood(settings)
		totaleatenprevday = foodatprevstart + foodInDay - foodatstart

		newday = True
		newfeedingtime = messageDecoder()
		foodInDay = foodTracker(settings, newfeedingtime, newday, foodInDay)
		SendMessageMeal(foodEaten, totaleatenprevday, foodInDay) #food sidpensed breakfast
		return [foodInDay, foodatstart]
		
	elif current_time == "12:00:00":
		foodEaten = 1-bowlFood(settings)
		foodatstart = foodatprevstart
		totaleatenprevday = foodatprevstart + foodInDay - foodatstart		sendMessageStats( foodEaten) #"It's lunch time for your dog, would you like to feed your dog? ", foofd eaten for breakfast
		newday = False
		newfeedingtime = messageDecoder()
		foodInDay = foodTracker(settings, newfeedingtime, newday, foodInDay)
		SendMessageMeal( foodEaten, eatensofartoday, foodInDay)#"Stats for this meal time, food dispensed and food left to be dispensed today:",
		return [foodInDay, foodatstart]
		
		
	elif current_time == "20:00:00":
		foodEaten = 1-bowlFood(settings)
		foodatstart= foodatprevstart
		newday = False
		newfeedingtime = messageDecoder()
		foodInDay = foodTracker(settings, newfeedingtime, newday, foodInDay)
		SendMessageMeal(foodEaten,eatensofartoday, foodInDay)#"Stats for this meal time, food dispensed and food left to be dispensed today:"
		return [foodInDay, foodatstart]
	
	
	else:
		foodatstart= foodatprevstart
		return [foodInDay, foodatstart]
	
		

# main code
#print("Start")

#while 1:

	# have time as a global variable
#	 
#	newday = False
#	newfeedingtime = False
	# poll function
#	feeding_time(newday, newfeedingtime)
