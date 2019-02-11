from messageDecoder import *

import paho.mqtt.client as mqtt

def scalerSetting():

	client = mqtt.Client()
	client.connect("test.mosquitto.org",port=1883)

	MSG_INFO = client.publish("IC.embedded/BGJR/test","Type what size dog you have, small medium or large:")
	mqtt.error_string(MSG_INFO.rc)

	if messageDecoder() == 1:
		return 5.5
	if messageDecoder() == 2:
		return 11
	if messageDecoder() == 3:
		return 16.5