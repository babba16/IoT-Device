from feeding_time import *
from dispensing import *
from settings import *
from messageDecoder import *
from petdetect import *

def main():
	foodInDay = 0
	settings = scalerSetting() #number to normalise sensor output equal to one unit of food
	stats = [0,0]
	
	while 1:
		stats = feeding_time(settings, stats[0], stats[1])
					
if __name__ == "__main__":
    main()
