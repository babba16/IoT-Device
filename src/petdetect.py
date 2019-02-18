from messageDecoder import *
from gpiozero import DigitalInputDevice


diginput=DigitalInputDevice(22)
def WhenActivated():
	data = "pet at bowl"
	sendMessageDogDetect(data)
def WhenDeactivated():
        data = "pet left bowl"
	sendMessageDogDetect(data)


diginput.when_activated=WhenActivated
diginput.when_deactivated = WhenDeactivated
			




