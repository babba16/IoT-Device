from messageDecoder import *

import json
import paho.mqtt.client as mqtt

def scalerSetting():

	client = mqtt.Client()
	client.connect("test.mosquitto.org",port=1883)

	MSG_INFO = client.publish("IC.embedded/BGJR/test", "a")#What mass of food in kg would you like your dog to eat in a day?
	mqtt.error_string(MSG_INFO.rc)
	
	selectedWeight = float(userData())
	
	scaler = (selectedWeight/3)*33 
	
	client = mqtt.Client()
	client.connect("test.mosquitto.org",port=1883)

	MSG_INFO = client.publish("IC.embedded/BGJR/test", ( selectedWeight/3))#"Ok, 1 unit of food is equal to "
	mqtt.error_string(MSG_INFO.rc)
	
	return scaler


def on_message(client,userdata,message) :
	print("Received message:{} on topic {}".format(message.payload, message.topic))
	global msg_recieved
	msg_recieved = (message.payload).decode("utf-8")
	client.loop_stop()
	
def userData():
	client = mqtt.Client()
	client.connect("test.mosquitto.org",port=1883)
	
	client.on_message = on_message
	client.subscribe("IC.embedded/BGJR/#")
	client.loop_start()
	time.sleep(15)
	return msg_recieved
