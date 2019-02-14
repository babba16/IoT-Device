import paho.mqtt.client as mqtt
import time
import json

print("start")
client = mqtt.Client()
print("abaout to connect")
client.connect("ee-estott-octo.ee.ic.ac.uk",port=1883)
print("Connected!")

msg_recieved = None

#------------receiving messages---------------#
def on_message(client,userdata,message) :
	print("Received message:{} on topic {}".format(message.payload, message.topic))
	global msg_recieved
	msg_recieved = (message.payload).decode("utf-8")
	client.loop_stop()

def compareCases(msg):
	if msg == 'no':
		return False
	elif msg == 'yes':
		return True
	else:
		client.publish("IC.embedded/BGJR/test","unknown input, please try again...")
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
def sendMessageMeal(foodEaten, eatensofartoday, foodInDay):
	client = mqtt.Client()
	client.connect("ee-estott-octo.ee.ic.ac.uk",port=1883)

	print(message) #testing
	data_dict = dict(id = "meal",time = time.ctime(), foodEaten = foodEaten, FoodEatenToday = eatensofartoday, FoodDispensedToday = foodInDay)
	data_out = json.dumps(data_dict)
	MSG_INFO = client.publish("IC.embedded/BGJR/test",data_out)
	mqtt.error_string(MSG_INFO.rc)

def sendMessageDogDetect(data):
	print("in right file")
	client = mqtt.Client()
	client.connect("ee-estott-octo.ee.ic.ac.uk",port=1883)

	print(data) #testing
	data_dict = dict(id = "Pet",time = time.ctime(), Data = data)
	data_out = json.dumps(data_dict)
	MSG_INFO = client.publish("IC.embedded/BGJR/test",data_out,qos=0)
	mqtt.error_string(MSG_INFO.rc)
	print("finished")


#---testing stuff----#
sendMessageDogDetect("Foo")
#print(messageDecoder())
