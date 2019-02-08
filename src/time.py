# prompt user to feed the dog @ 8am, 12pm, 8pm

import time

# function to check set feeding times
def feeding_time(newday, newfeedingtime):

	# prompt user to feed dog at 8am, 12pm, 8pm
	if current_time == "08:00:00":
		sendMessage("It's breakfast time for your dog")
		newfeedingtime = True
		if newfeedingtime == True:
			newday = True    # newday set to true upon first feeding
#			print("newday: " + str(newday))
	elif current_time == "12:00:00":
		sendMessage("It's lunch time for your dog")
		newfeedingtime = True
	elif current_time == "20:00:00":
		sendMessage("It's dinner time for your dog")
		newfeedingtime = True

# main code
print("Start")

while 1:

	# have time as a global variable
	current_time = time.strftime("%H:%M:%S") 
	newday = False
	newfeedingtime = False
	# poll function
	feeding_time(newday, newfeedingtime)

