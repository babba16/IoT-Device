import smbus

bus = smbus.SMBus(1)
mealLimit = 1
maxDayLimit = 3
foodInDay = 0
scaler = 11 #needs to be updated

bus.write_i2c_block_data(0x48,0x01,[0x88, 0x83]) # configure sensor

def foodTracker(newfeedingtime, newday):

	if newday == True:
		dayLimit = maxDayLimit - bowlFood()
		foodInDay = 0
		
	if newfeedingtime == True and dayLimit > 0:
		dayLimit = dayLimit - dispenseFood()
		foodInDay = foodInDay + dispenseFood()
		
def dispenseFood(): #dispenses required amount of food for meal and returns the amount dispensed in thisMeal
	thisMeal = mealLimit - bowlFood()
	#TODO: needs to be drive LED to represent motor
	while  bowlFood() < thisMeal:
		print bowlFood() #for testing, allows us to continuously see the value of the weight applied to sensor. 
	return thisMeal
	
	
def bowlFood(): # go to sensor to get the weight of the food in the bowl
	#read data from ADC
	data = int.from_bytes(bus.read_i2c_block_data(0x48,0x00,2),"big")
	scaledData = (65531-data)/scaler
	return scaledData
