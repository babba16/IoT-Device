import paho.mqtt.client as mqtt
import time

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
	else:
		return True
		
def messageDecoder(): 
	client.on_message = on_message
	client.subscribe("IC.embedded/BGJ/#")
	client.loop_start()
	time.sleep(15)
	return compareCases(msg_recieved)
	
		
		
#------------sending messages---------------#		
def sendMessage(message): #sending messages
	print(message) #testing
	MSG_INFO = client.publish("IC.embedded/BGJ/test",message)
	#mqtt.error_string(MSG_INFO.rc)
	#client.tls_set(ca_certs="mosquitto.org.crt",certfile="client.crt",keyfile="client.key")

#---testing stuff----#
#sendMessage("Foo")
#print(messageDecoder())