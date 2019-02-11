from messageDecoder import *

import json
import paho.mqtt.client as mqtt

def scalerSetting():

	client = mqtt.Client()
	client.connect("test.mosquitto.org",port=1883)

	MSG_INFO = client.publish("IC.embedded/BGJR/test", "Type what size dog you have, small medium or large:")
	mqtt.error_string(MSG_INFO.rc)
	
	data = dict(small = "0.5kg a day = 3 units, 1 unit per meal", medium = "1kg a day = 3 units, 1 unit per meal", large = "1.5kg a day = 3 units, 1 unit per meal")
	data_out = json.dumps(data)
	MSG_INFO = client.publish("IC.embedded/BGJR/test", data_out)
	mqtt.error_string(MSG_INFO.rc)

	if messageDecoder() == 1:
		return 5.5
	if messageDecoder() == 2:
		return 11
	if messageDecoder() == 3:
		return 16.5
