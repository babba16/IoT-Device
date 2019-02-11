import paho.mqtt.client as mqtt
import time
import json

client = mqtt.Client()
client.connect("test.mosquitto.org",port=1883)

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
	elif msg == 'small'
		return 1
	elif msg == 'medium'
		return 2
	elif msg == 'large'
		return 3
	else
		client.publish("IC.embedded/BGJR/test","unknown input, please try again...")
		messageDecoder()
		
def messageDecoder(): 
	client = mqtt.Client()
	client.connect("test.mosquitto.org",port=1883)
	
	client.on_message = on_message
	client.subscribe("IC.embedded/BGJR/#")
	client.loop_start()
	time.sleep(15)
	return compareCases(msg_recieved)
	
		
		
#------------sending messages---------------#		
def sendMessage(message,foodEaten,foodLeft): #sending messages
	client = mqtt.Client()
	client.connect("test.mosquitto.org",port=1883)
	
	print(message) #testing
	data_dict = dict(time = time.ctime(), message = message, FoodEaten = foodEaten, FoodLeft = foodLeft)
	data_out = json.dumps(data_dict)
	MSG_INFO = client.publish("IC.embedded/BGJR/test",data_out)
	mqtt.error_string(MSG_INFO.rc)
	#client.tls_set(ca_certs="mosquitto.org.crt",certfile="client.crt",keyfile="client.key")

#---testing stuff----#
#sendMessage("Foo")
#print(messageDecoder())
