function getTargetTime(hour){
	var t = new Date();
	t.setHours(hour);
	t.setMinutes(0);
	t.setSeconds(0);
	t.setMilliseconds(0);
	return t;
}

var targetTimeBreakfast = getTargetTime(8).getTime();
var targetTimeLunch = getTargetTime(12).getTime();
var targetTimeDinner = getTargetTime(20).getTime();

var timeNow =  new Date().getTime();

var timeOffsetBreakfast = targetTimeBreakfast - timeNow;
var timeOffsetLunch = targetTimeLunch - timeNow;
var timeOffsetDinner = targetTimeDinner - timeNow;


if (timeOffsetBreakfast >= 0){
	setTimeout(function(){promptUser("breakfast");}, timeOffsetBreakfast);
}

if (timeOffsetLunch >= 0){
	setTimeout(function(){promptUser("lunch");}, timeOffsetLunch);
}

if (timeOffsetDinner >= 0){
	setTimeout(function(){promptUser("dinner");}, timeOffsetDinner);
}
