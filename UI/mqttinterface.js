// Embedded Systems
// Team BGJR
// IoT Device JS for data handling in user innterface



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

// message sending function
function messageSend(msg) {
	message = new Paho.MQTT.Message(msg);
	message.destinationName = "IC.embedded/BGJR/";
	client.send(message);
}

// displays prompt and enables 'yes' and 'no' buttons
function promptUser(time) {
	document.getElementById("prompts").innerHTML = "It's time for " + time + ". Would you like to feed your dog now?";
	document.getElementById("promptButton1").style.display = "inline-block";
	document.getElementById("promptButton2").style.display = "inline-block";
}

// formats output to webpage based on received mqtt data
function messageFormat(msg){
	// 'yes' or 'no' message sent from interface - sets sendInfo to 'Done' to confirm message sent
	if ((msg == "yes") || (msg == "no")){
		document.getElementById("sendInfo").innerHTML = "Info: Done";
	}
	// massPrompt sent from pi means input settings data
	else if (msg == "massPrompt"){
		setUp();
	}
	// JSON object contains 'id' field
	else if (msg.includes("id")){
		msg1 = JSON.parse(msg);
		// stats message
		if (msg1.id == 'stats') {
			document.getElementById("latest").innerHTML = "Latest Update at: " + msg1.time;
			document.getElementById("field1").innerHTML = "Food Eaten: " + msg1.FoodEaten;
			document.getElementById("field2").innerHTML = "Food Left: " + msg1.FoodLeft;
		}
		// mealtime message
		else if (msg1.id == 'meal'){
			document.getElementById("latest").innerHTML = "Mealtime Info at: " + msg1.time;
			document.getElementById("field1").innerHTML = "Food Dispensed: " + msg1.TotalDispensed;
			document.getElementById("field2").innerHTML = "Food to be Dispensed: " + msg1.FoodToBeDispensed;
			hidePrompt();
		}
		// pet is at bowl message (from movement sensor)
		else if (msg1.id == 'Pet'){
			shiftUpdate();
			document.getElementById("field1").innerHTML = "Dog Last at Bowl at: " + msg1.time;
		}
	}
	// always print raw MQTT message into sendInfo
 	document.getElementById("sendInfo").innerHTML = "Info: Incoming MQTT data: " + msg;
}

// rehide prompt and buttons after user interaction
function hidePrompt(){
	document.getElementById("prompts").innerHTML = ""
	document.getElementById("promptButton1").style.display = "none";
	document.getElementById("promptButton2").style.display = "none";
}

// display settings form for inputting daily food amount
function setUp() {
	document.getElementById("SettingsHeader").style.display = "inline-block";
	document.getElementById("SettingsPrompt").style.display = "inline-block";
	document.getElementById("SettingsForm").style.display = "inline-block";
}

// function to rehide the settings form
function hideSetUp() {
	document.getElementById("SettingsHeader").style.display = "none";
	document.getElementById("SettingsPrompt").style.display = "none";
	document.getElementById("SettingsForm").style.display = "none";
}
