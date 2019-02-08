import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect("test.mosquitto.org",port=1883)

#------------receiving messages---------------
def on_message(client,userdata,message) :
	print("Received message:{} on topic {}".format(message.payload, message.topic))
	return message.payload

def messageDecoder(): 
	client.on_message = on_message
	client.subscribe("IC.embedded/BGJR/#")
	client.loop_start()

	if client.on_message == 'no':
		client.loop_stop()
		return False
	else:
		client.loop_stop()
		return True
		
		
#------------sending messages---------------		
def sendMessage(message): #sending messages
	MSG_INFO = client.publish("IC.embedded/BGJR/test",message)
	mqtt.error_string(MSG_INFO.rc)
	client.tls_set(ca_certs="mosquitto.org.crt",certfile="client.crt",keyfile="client.key")


