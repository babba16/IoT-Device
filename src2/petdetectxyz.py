
from gpiozero import DigitalInputDevice


diginput=DigitalInputDevice(22)
def WhenActivated():
	
       print("dog came to bowl")
def WhenDeactivated():
        print("dog left bowl")


diginput.when_activated=WhenActivated
diginput.when_deactivated = WhenDeactivated
			




