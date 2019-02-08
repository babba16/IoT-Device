import smbus
import time


bus = smbus.SMBus(1)
mealLimit = 1
maxDayLimit = 3
foodInDay = 0
scaler = 1 #needs to be updated




def foodTracker(newfeedingtime, newday):

	if newday == true:
		dayLimit = maxDayLimit - bowlFood()
		foodInDay = 0
		
	if newfeedingtime == true && dayLimit > 0:
		thisMeal = dispenseFood()
		dayLimit = dayLimit - thisMeal
		foodInDay = foodInDay + thisMeal
		
		
def dispenseFood(): #dispenses required amount of food for meal and returns the amount dispensed in thisMeal
	thisMeal = mealLimit - bowlFood()
	while  bowlFood() < thisMeal:
		#add food to bowl
	return thisMeal
	

def bowlFood(): # go to sensor to get the weight of the food in the bowl
	#read data from ADC
	data = int.from_bytes(bus.read_i2c_block_data(0x48,0x00,2))
	weightOfFood = data/scaler #scaler needs to be found to map the data to a weight
	return weightOfFood
