// Create a client instance
client = new Paho.MQTT.Client("test.mosquitto.org", 8080, "clientId");

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
}

function messageSend(msg) {
	message = new Paho.MQTT.Message(msg);
	message.destinationName = "IC.embedded/BGJR/";
	client.send(message);
	//document.getElementById("sendInfo").innerHTML = "Done";
}

// displays prompt and enables 'yes' and 'no' buttons
function promptUser(time) {
	document.getElementById("prompts").innerHTML = "It's time for " + time + ". Would you like to feed your dog now?";
	document.getElementById("promptButton1").style.display = "inline-block";
	document.getElementById("promptButton2").style.display = "inline-block";
}

// formats output to webpage based on received mqtt data
function messageFormat(msg){
	if ((msg == "yes") || (msg == "no")){
		document.getElementById("sendInfo").innerHTML = "Info: Done";
	}
	else if (msg == "massPrompt"){
		setUp();
	}
	else if (msg.includes("id")){
		msg1 = JSON.parse(msg);
		if (msg1.id == 'stats') {
			document.getElementById("latest").innerHTML = "Latest Update at: " + msg1.time;
			document.getElementById("field1").innerHTML = "Food Eaten: " + msg1.FoodEaten;
			document.getElementById("field2").innerHTML = "Food Left: " + msg1.FoodLeft;
		}
		else if (msg1.id == 'meal'){
			document.getElementById("latest").innerHTML = "Mealtime Info at: " + msg1.time;
			document.getElementById("field1").innerHTML = "Food Dispensed: " + msg1.TotalDispensed;
			document.getElementById("field2").innerHTML = "Food to be Dispensed: " + msg1.FoodToBeDispensed;
			hidePrompt();
		}
		else if (msg1.id == 'Pet'){
			shiftUpdate();
			document.getElementById("field1").innerHTML = "Dog Last at Bowl at: " + msg1.time;
		}
	}
 	document.getElementById("sendInfo").innerHTML = "Info: Incoming MQTT data: " + msg;
}

// rehide prompt and buttons after user interaction
function hidePrompt(){
	document.getElementById("prompts").innerHTML = ""
	document.getElementById("promptButton1").style.display = "none";
	document.getElementById("promptButton2").style.display = "none";
}

function setUp() {
	document.getElementById("SettingsHeader").style.display = "inline-block";
	document.getElementById("SettingsPrompt").style.display = "inline-block";
	document.getElementById("SettingsForm").style.display = "inline-block";
}

function hideSetUp() {
	document.getElementById("SettingsHeader").style.display = "none";
	document.getElementById("SettingsPrompt").style.display = "none";
	document.getElementById("SettingsForm").style.display = "none";
}
