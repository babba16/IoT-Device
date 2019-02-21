import paho.mqtt.client as mqtt
import time
import json

client = mqtt.Client()
client.connect("ee-estott-octo.ee.ic.ac.uk",port=1883)

msg_recieved = None

#------------receiving messages---------------#
def on_message(client,userdata,message) :
	print("Received message:{} on topic {}".format(message.payload, message.topic))
	global msg_recieved
	msg_recieved = (message.payload).decode("utf-8")
	client.loop_stop()

def compareCases(msg):
#different user input options handled here:
	if msg == 'no':
		return False
	elif msg == 'yes':
		return True
	else:
		#unknown input
		messageDecoder()

def messageDecoder():
	client = mqtt.Client()
	client.connect("ee-estott-octo.ee.ic.ac.uk",port=1883)

	client.on_message = on_message
	client.subscribe("IC.embedded/BGJR/#")
	client.loop_start()
	time.sleep(15)
	return compareCases(msg_recieved)



#------------sending messages---------------#
#message for food stats
def sendMessageMeal(foodEaten, eatensofartoday, foodInDay):
	client = mqtt.Client()
	client.connect("ee-estott-octo.ee.ic.ac.uk",port=1883)

	data_dict = dict(id = "meal",time = time.ctime(), foodEaten = foodEaten, FoodEatenToday = eatensofartoday, FoodDispensedToday = foodInDay)
	data_out = json.dumps(data_dict)
	MSG_INFO = client.publish("IC.embedded/BGJR/test",data_out)
	mqtt.error_string(MSG_INFO.rc)

#message for detecting pet at bowl.
def sendMessageDogDetect(data):
	client = mqtt.Client()
	client.connect("ee-estott-octo.ee.ic.ac.uk",port=1883)

	print(data) #testing
	data_dict = dict(id = "Pet",time = time.ctime(), Data = data)
	data_out = json.dumps(data_dict)
	MSG_INFO = client.publish("IC.embedded/BGJR/test",data_out)
	mqtt.error_string(MSG_INFO.rc)


#---testing stuff----#
#sendMessageDogDetect("Foo")
#print(messageDecoder())
