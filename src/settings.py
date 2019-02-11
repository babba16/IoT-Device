from messageDecoder import *

import json
import paho.mqtt.client as mqtt

def scalerSetting():

	client = mqtt.Client()
	client.connect("test.mosquitto.org",port=1883)

	MSG_INFO = client.publish("IC.embedded/BGJR/test", "Type what size dog you have, small medium or large:")
	mqtt.error_string(MSG_INFO.rc)

	if messageDecoder() == 1:
		client = mqtt.Client()
		client.connect("test.mosquitto.org",port=1883)
		client.publish("IC.embedded/BGJR/test", "Small: 0.5kg of food a day = 3 units split into 1 unit per meal.")
		return 5.5
	if messageDecoder() == 2:
		client = mqtt.Client()
		client.connect("test.mosquitto.org",port=1883)
		client.publish("IC.embedded/BGJR/test", "Medium: 1kg of food a day = 3 units split into 1 unit per meal.")
		return 11
	if messageDecoder() == 3:
		client = mqtt.Client()
		client.connect("test.mosquitto.org",port=1883)
		client.publish("IC.embedded/BGJR/test", "Large: 1.5kg of food a day = 3 units split into 1 unit per meal.")
		return 16.5
	
