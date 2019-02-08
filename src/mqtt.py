import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect("test.mosquitto.org",port=1883)
MSG_INFO = client.publish("IC.embedded/BGJR/test","hello") #sends data to website or whatever
mqtt.error_string(MSG_INFO.rc) #says if there is an error
client.tls_set(ca_certs="mosquitto.org.crt",certfile="client.crt",keyfile="client.key")

def on_message(client,userdata,message) :
	print("Received message:{} on topic {}".format(message.payload, message.topic))

client.on_message = on_message
client.subscribe("IC.embedded/BGJR/#")
client.loop_forever() #regularly checks for updates, accesses on_message to print what has been received
