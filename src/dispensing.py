import smbus

bus = smbus.SMBus(1)
mealLimit = 1
maxDayLimit = 3
foodInDay = 0
scaler = 1 #needs to be updated

def foodTracker(newfeedingtime, newday):

	if newday == True:
		dayLimit = maxDayLimit - bowlFood()
		foodInDay = 0
		
	if newfeedingtime == True and dayLimit > 0:
		dayLimit = dayLimit - dispenseFood()
		foodInDay = foodInDay + dispenseFood()
		
def dispenseFood(): #dispenses required amount of food for meal and returns the amount dispensed in thisMeal
	thisMeal = mealLimit - bowlFood()
	while  bowlFood() < thisMeal:
		foo=1 #TODO: needs to be drive LED to represent motor
	return thisMeal
	
bus.write_i2c_block_data(0x48,0x01,[0x88, 0x83]) # write to it once with config
	
def bowlFood(): # go to sensor to get the weight of the food in the bowl
	#read data from ADC
	data = int.from_bytes(bus.read_i2c_block_data(0x48,0x00,2),"big")
	weightOfFood = data/scaler #scaler needs to be found to map the data to a weight
	return weightOfFood
