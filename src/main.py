from feeding_time import *
from dispensing import *
from settings import *
from messageDecoder import *

def main():
	foodInDay = 0
	dayLimit = 3
	settings = scalerSetting()
	
	feeding_time(settings, foodInDay, dayLimit)
			
if __name__ == "__main__":
    main()
