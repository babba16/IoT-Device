# prompt user to feed the dog @ 8am, 12pm, 8pm
from messageDecoder import *
from dispensing import *
import time

# function to check set feeding times
def feeding_time(settings, foodInDay, foodatprevstart):
	current_time = time.strftime("%H:%M:%S")
	# prompt user to feed dog at 8am, 12pm, 8pm
	if current_time == "09:00:00":
		foodEaten = 1 - bowlFood(settings) #food eaten previous meal.
		foodatstart = bowlFood(settings) #food at start of current meal
		totaleatenprevday = foodatprevstart + foodInDay - foodatstart #total food eaten yesterday
		newday = True
		newfeedingtime = messageDecoder() #get input from user, check whether to feed pet.
		foodInDay = foodTracker(settings, newfeedingtime, newday, foodInDay) #get food dispensed so far
		SendMessageMeal(foodEaten, totaleatenprevday, foodInDay) #food dispensed breakfast
		return [foodInDay, foodatstart]
		
	elif current_time == "12:00:00":
		foodEaten = 1-bowlFood(settings) #food eaten previous meal.
		foodatstart = foodatprevstart #food at start of current meal
		totaleatenprevday = foodatprevstart + foodInDay - foodatstart #total food eaten so far.
		newday = False
		newfeedingtime = messageDecoder() #get input from user, check whether to feed pet.
		foodInDay = foodTracker(settings, newfeedingtime, newday, foodInDay) #get food dispensed so far
		SendMessageMeal( foodEaten, eatensofartoday, foodInDay) #food dispensed lunch
		return [foodInDay, foodatstart]
		
		
	elif current_time == "20:00:00":
		foodEaten = 1-bowlFood(settings) #food eaten previous meal.
		foodatstart = foodatprevstart #food at start of current meal
		totaleatenprevday = foodatprevstart + foodInDay - foodatstart #total food eaten so far.
		newday = False
		newfeedingtime = messageDecoder() #get input from user, check whether to feed pet.
		foodInDay = foodTracker(settings, newfeedingtime, newday, foodInDay)  #get food dispensed so far
		SendMessageMeal(foodEaten,eatensofartoday, foodInDay) #food dispensed dinner
		return [foodInDay, foodatstart]
	
	
	else:
		foodatstart = foodatprevstart
		return [foodInDay, foodatstart]
