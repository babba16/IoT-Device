import smbus
import time

bus = smbus.SMBus(1)
mealLimit = 1

bus.write_i2c_block_data(0x48,0x01,[0x88, 0x83]) # configure sensor

def foodTracker(settings, newfeedingtime, newday, foodInDay):
	if newday == True:
		print("It's a new day")
		foodInDay = 0
		
	if newfeedingtime == True:
		print ("Food time!")
		print(mealLimit)
		thisMeal = mealLimit - bowlFood(settings)
		#TODO: needs to be drive LED to represent motor
		while  bowlFood(settings) < mealLimit:
			print(bowlFood(settings)) #for testing, allows us to continuously see the value of the weight applied to sensor. 
			time.sleep(1)
		foodInDay = foodInDay + thisMeal
		
	return foodInDay
	
	
def bowlFood(scalar): # go to sensor to get the weight of the food in the bowl
	#read data from ADC
	data = int.from_bytes(bus.read_i2c_block_data(0x48,0x00,2),"big")
	scaledData = (65531-data)/scaler
	return scaledData