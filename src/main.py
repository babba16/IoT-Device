from feeding_time import *
from dispensing import *
from settings import *
from messageDecoder import *

def main():
	foodInDay = 0
	settings = scalerSetting() #equal to one unit of food
	
	while 1:
		foodInDay = feeding_time(settings, foodInDay)
		print(foodInDay)
			
if __name__ == "__main__":
    main()
