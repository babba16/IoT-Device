# prompt user to feed the dog @ 8am, 12pm, 8pm
from messageDecoder import *
from fullscript import *
import time

# function to check set feeding times
def feeding_time(newday, newfeedingtime, foodInDay):
	current_time = time.strftime("%H:%M:%S")
	# prompt user to feed dog at 8am, 12pm, 8pm
	if current_time != "15:31:00":
		sendMessage("It's breakfast time for your dog, would you like to feed your dog? ", foodInDay)
		newday = True
		newfeedingtime = messageDecoder()
		foodTracker(newfeedingtime, newday)
	elif current_time == "12:00:00":
		sendMessage("It's lunch time for your dog, would you like to feed your dog? ", foodInDay)
		newday = False
		newfeedingtime = messageDecoder()
		foodTracker(newfeedingtime, newday)
		
	elif current_time == "20:00:00":
		sendMessage("It's dinner time for your dog, would you like to feed your dog? ", foodInDay")
		newday = False
		newfeedingtime = messageDecoder()
		foodTracker(newfeedingtime, newday)
		

# main code
#print("Start")

#while 1:

	# have time as a global variable
#	 
#	newday = False
#	newfeedingtime = False
	# poll function
#	feeding_time(newday, newfeedingtime)

