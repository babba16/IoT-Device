import smbus
import time
from gpiozero import LED
bus = smbus.SMBus(1)


bus.write_i2c_block_data(0x48,0x01,[0x88, 0x83]) # configure sensor

#dispenses food and gets the food dispensed in the day.
def foodTracker(settings, newfeedingtime, newday, foodInDay):
	if newday == True:
		print("It's a new day")
		foodInDay = 0
		
	if newfeedingtime == True:
		led = LED(17)
		thisMeal = 1 - bowlFood(settings)
		
		while  bowlFood(settings) < 1:
			print(bowlFood(settings)) #for testing, allows us to continuously see the value of the weight applied to sensor. 
			led.on() #led is on while food is left to be put into bowl.
		led.off()
		foodInDay = foodInDay + thisMeal
		
	return foodInDay
	
#interacts with sensor and normalises data.	
def bowlFood(scalar): # go to sensor to get the weight of the food in the bowl
	#read data from ADC
	data = int.from_bytes(bus.read_i2c_block_data(0x48,0x00,2),"big")
	scaledData = (65531-data)/scalar #normalises data
	return scaledData
