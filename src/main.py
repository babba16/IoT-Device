from feeding_timexyz import *
from dispensing import *
from settingsxyz import *
#from messageDecoder import *
from petdetectxyz import *

def main():
	foodInDay = 0
	settings = scalerSetting() #equal to one unit of food
	stats = [0,0]
	
	while 1:
		stats = feeding_time(settings, stats[0], stats[1])
					
if __name__ == "__main__":
    main()
