from feeding_time import *
from dispensing import *
from messageDecoder import *

def main():
	newday = False
	newfeedingtime = False
	foodInDay = 0
	while 1:
		feeding_time(newday,newfeedingtime,foodInDay)
			
if __name__ == "__main__":
    main()