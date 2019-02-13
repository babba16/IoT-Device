// Create a client instance
client = new Paho.MQTT.Client("ee-estott-octo.ee.ic.ac.uk", 8080, "clientId");

// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

// connect the client
client.connect({onSuccess:onConnect});

// called when the client connects
function onConnect() {
	// Once a connection has been made, make a subscription and send a message.
	console.log("onConnect");
	client.subscribe("IC.embedded/BGJR/#");
}

// called when the client loses its connection
function onConnectionLost(responseObject) {
	if (responseObject.errorCode !== 0) {
		console.log("onConnectionLost:"+responseObject.errorMessage);
	}
}

// called when a message arrives
function onMessageArrived(message) {
	console.log("onMessageArrived:"+message.payloadString);
	messageFormat(message.payloadString);
	if (messageDecoder(message.payloadString)) {
		promptUser();
	}
}

function messageSend(msg) {
	message = new Paho.MQTT.Message(msg);
	message.destinationName = "IC.embedded/BGJR/";
	client.send(message);
	//document.getElementById("sendInfo").innerHTML = "Done";
}

// reads mqtt data and returns true if a prompt is required
function messageDecoder(msg) {
	if ((msg == "yes") || (msg == "no")) { // if its a feeding time
		return false;
	}
	else {
		return true;
	}
}

// displays prompt and enables 'yes' and 'no' buttons
function promptUser() {
	document.getElementById("prompts").innerHTML = "Would you like to feed your dog now?";
	document.getElementById("promptButton1").style.display = "inline-block";
	document.getElementById("promptButton2").style.display = "inline-block";
}

// formats output to webpage based on received mqtt data
function messageFormat(msg){
	if ((msg == "yes") || (msg == "no")){
		document.getElementById("sendInfo").innerHTML = "Info: Done";
	}
	//else {
	//	msg = json.parse(msg);
	//	document.getElementById("latest").innerHTML =
	// 		"Latest Update for " + msg.time\n
	//}
	else {
		document.getElementById("sendInfo").innerHTML = "Info: MQTT data: " + msg;
	}
}

// rehide prompt and buttons after user interaction
function hidePrompt(){
	document.getElementById("prompts").innerHTML = ""
	document.getElementById("promptButton1").style.display = "none";
	document.getElementById("promptButton2").style.display = "none";
}
