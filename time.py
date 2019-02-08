# prompt user to feed the dog @ 8am, 12pm, 8pm
# def problems with this in terms of implementing with the rest
# of the code so this is just a basis i guess 

import time

# prompts user to feed dog y/n
def prompt_feed (newfeedingtime):
	if input("Would you like to feed now?") == 'y':
		newfeedingtime = True
	else:
		newfeedingtime = False
	print("newfeedingtime: " + str(newfeedingtime))
	return newfeedingtime

# function to check set feeding times
def feeding_time(newday, newfeedingtime):

	# prompt user to feed dog at 8am, 12pm, 8pm
	if current_time == "08:00:00":
		print("It's breakfast time for your dog")
		newfeedingtime = prompt_feed(newfeedingtime)
		if newfeedingtime == True:
			newday = True    # newday set to true upon first feeding
			print("newday: " + str(newday))
	elif current_time == "12:00:00":
		print("It's lunch time for your dog")
		newfeedingtime = prompt_feed(newfeedingtime)
	elif current_time == "20:00:00":
		print("It's dinner time for your dog")
		newfeedingtim = prompt_feed(newfeedingtime)



# main code
print("Start")

while 1:

	# have time as a global variable
	current_time = time.strftime("%H:%M:%S")
	newday = False
	newfeedingtime = False
	# poll function
	feeding_time(newday, newfeedingtime)
