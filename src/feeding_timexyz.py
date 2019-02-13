# prompt user to feed the dog @ 8am, 12pm, 8pm
from messageDecoder import *
from dispensing import *
import time

#maxDayLimit = 3

# function to check set feeding times
def feeding_time(settings, foodInDay):
	current_time = time.strftime("%H:%M:%S")
	# prompt user to feed dog at 8am, 12pm, 8pm
	if current_time != "15:31:00":
		#send foodinday from previous day - food dispensed previous day was..
		
		#sendMessageStats(0, maxDayLimit) #"It's breakfast time for your dog, would you like to feed your dog? "
		print("It's breakfast time for your dog, would you like to feed your dog? ")
		newday = True
		#newfeedingtime = messageDecoder()
		newfeedingtime= True
		foodInDay = foodTracker(settings, newfeedingtime, newday, foodInDay)
		#SendMessageMeal(foodInDay) #food sidpensed breakfast
		print ("food dispensed breakfast")
		print (foodInDay)
		return foodInDay
		
	elif current_time == "12:00:00":
		foodEaten = 1-bowlFood(settings)
		foodLeft = maxDayLimit - foodEaten
		#sendMessageStats( foodEaten) #"It's lunch time for your dog, would you like to feed your dog? ", foofd eaten for breakfast
		
		print("It's lunch time for your dog, would you like to feed your dog? ")
		newday = False
		#newfeedingtime = messageDecoder()
		newfeedingtime = True
		foodInDay = foodTracker(settings, newfeedingtime, newday, foodInDay)
		#SendMessageMeal( foodInDay)#"Stats for this meal time, food dispensed and food left to be dispensed today:",
		print("Stats for this meal time, food dispensed")
		print (foodInDay)
		return foodInDay
		
		
	elif current_time == "20:00:00":
		foodEaten = 1-bowlFood(settings)
		#foodLeft = maxDayLimit - foodEaten
		#sendMessageStats( foodEaten) # food eaten is food eaten at lunch, "It's dinner time for your dog, would you like to feed your dog? ",
		print ("It's dinner time for your dog")
		newday = False
		newfeedingtime = True
		foodInDay = foodTracker(settings, newfeedingtime, newday, foodInDay)
		print("Stats for this meal time, food dispensed")
		print (foodInDay)
		return foodInDay
	
	
	else:
		return foodInDay
	
		

# main code
#print("Start")

#while 1:

	# have time as a global variable
#	 
#	newday = False
#	newfeedingtime = False
	# poll function
#	feeding_time(newday, newfeedingtime)