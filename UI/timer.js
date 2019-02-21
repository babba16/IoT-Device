
// formats the target time
function getTargetTime(hour){
	var t = new Date();
	t.setHours(hour);
	t.setMinutes(0);
	t.setSeconds(0);
	t.setMilliseconds(0);
	return t;
}

// sets mealtimes
var targetTimeBreakfast = getTargetTime(8).getTime();
var targetTimeLunch = getTargetTime(12).getTime();
var targetTimeDinner = getTargetTime(20).getTime();

var timeNow =  new Date().getTime();

// time offset is number of seconds from now until the target time
var timeOffsetBreakfast = targetTimeBreakfast - timeNow;
var timeOffsetLunch = targetTimeLunch - timeNow;
var timeOffsetDinner = targetTimeDinner - timeNow;

// sets a timeout for the next mealtime if the current time is before that time
if (timeOffsetBreakfast >= 0){
	setTimeout(function(){promptUser("breakfast");}, timeOffsetBreakfast);
}

if (timeOffsetLunch >= 0){
	setTimeout(function(){promptUser("lunch");}, timeOffsetLunch);
}

if (timeOffsetDinner >= 0){
	setTimeout(function(){promptUser("dinner");}, timeOffsetDinner);
}
