# prompt user to feed the dog @ 8am, 12pm, 8pm
from messageDecoder import *
from dispensing import *
import time

maxDayLimit = 3

# function to check set feeding times
def feeding_time(settings, foodInDay):
	current_time = time.strftime("%H:%M:%S")
	# prompt user to feed dog at 8am, 12pm, 8pm
	if current_time != "15:31:00":
		sendMessageStats("It's breakfast time for your dog, would you like to feed your dog? ", 0, maxDayLimit)
		newday = True
		newfeedingtime = messageDecoder()
		foodInDay = foodTracker(settings, newfeedingtime, newday, foodInDay)
		SendMessageMeal("Stats for today:", foodInDay)
		
	elif current_time == "12:00:00":
		foodEaten = 1-bowlFood(settings)
		foodLeft = maxDayLimit - foodEaten
		sendMessageStats("It's lunch time for your dog, would you like to feed your dog? ", foodEaten, foodLeft)
		newday = False
		newfeedingtime = messageDecoder()
		foodInDay = foodTracker(settings, newfeedingtime, newday, foodInDay)
		SendMessageMeal("Stats for this meal time, food dispensed and food left to be dispensed today:", foodInDay)
		
	elif current_time == "20:00:00":
		foodEaten = 2-bowlFood(settings)
		foodLeft = maxDayLimit - foodEaten
		sendMessageStats("It's dinner time for your dog, would you like to feed your dog? ", foodEaten, foodLeft)
		newday = False
		newfeedingtime = messageDecoder()
		foodInDay = foodTracker(settings, newfeedingtime, newday, foodInDay)
		SendMessageMeal("Stats for this meal time, food dispensed and food left to be dispensed today:", foodInDay)
		
	
		

# main code
#print("Start")

#while 1:

	# have time as a global variable
#	 
#	newday = False
#	newfeedingtime = False
	# poll function
#	feeding_time(newday, newfeedingtime)

