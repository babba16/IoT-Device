# prompt user to feed the dog @ 8am, 12pm, 8pm

from dispensing import *
import time

#maxDayLimit = 3

# function to check set feeding times
def feeding_time(settings, foodInDay,foodatprevstart):
	current_time = time.strftime("%H:%M:%S")
	# prompt user to feed dog at 8am, 12pm, 8pm
	if current_time == "09:57:00":
		
		foodEaten = 1 - bowlFood(settings)
		foodatstart = bowlFood(settings)
		totaleatenprevday = foodatprevstart + foodInDay - foodatstart




		print("It's breakfast time for your dog, would you like to feed your dog? ")
		newday = True
		#newfeedingtime = messageDecoder()
		newfeedingtime= True
		foodInDay = foodTracker(settings, newfeedingtime, newday, foodInDay)
		#SendMessageMeal(foodEaten,totaleatenprevday, foodInDay) #food sidpensed breakfast
		print("Stats for the day, food eaten previous meal,previous day, food dispensed", foodEaten, totaleatenprevday,  foodInDay)
		return [foodInDay, foodatstart]
		
	elif current_time == "09:57:30":
		foodEaten = 1-bowlFood(settings)
		foodatstart= foodatprevstart
		eatensofartoday = foodatprevstart + foodInDay - foodatstart
		
		print("It's lunch time for your dog, would you like to feed your dog? ")
		newday = False
		#newfeedingtime = messageDecoder()
		newfeedingtime = True
		foodInDay = foodTracker(settings, newfeedingtime, newday, foodInDay)
		#SendMessageMeal(foodEaten,eatensofartoday foodInDay)#"Stats for this meal time, food dispensed and food left to be dispensed today:",
		print("Stats for the day, food eaten previous meal, eatensofartoday, food dispensed", foodEaten, eatensofartoday,  foodInDay)
		return [foodInDay, foodatstart]
		
		
	elif current_time == "09:58:00":
		foodEaten = 1-bowlFood(settings)
		foodatstart= foodatprevstart
		eatensofartoday = foodatprevstart + foodInDay - foodatstart
		print ("It's dinner time for your dog")
		newday = False
		#newfeedingtime = messageDecoder()
		newfeedingtime = True
		foodInDay = foodTracker(settings, newfeedingtime, newday, foodInDay)
		print("Stats for the day, food eaten previous meal, eatensofartoday, food dispensed", foodEaten, eatensofartoday,  foodInDay)
		#SendMessageMeal(foodEaten,eatensofartoday, foodInDay)#"Stats for this meal time, food dispensed and food left to be dispensed today:",
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
