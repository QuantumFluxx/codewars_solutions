## Description:

Story
Due to lack of maintenance the minute-hand has fallen off Town Hall clock face.

And because the local council has lost most of our tax money to a Nigerian email scam there are no funds to fix the clock properly.

Instead, they are asking for volunteer programmers to write some code that tell the time by only looking at the remaining hour-hand!

What a bunch of cheapskates!

Can you do it?

Kata
Given the angle (in degrees) of the hour-hand, return the time in 12 hour HH:MM format. Round down to the nearest minute.

### Examples (input --> output):
```
12:00 = 0 degrees

03:00 = 90 degrees

06:00 = 180 degrees

09:00 = 270 degrees

12:00 = 360 degrees
```

 ## Solution:
 
```javascript
var whatTimeIsIt = function(angle) {
  let angleFloor = angle;
  let minutes = Math.floor((angleFloor % 30) * 2);
  let hours = Math.floor(angleFloor / 30);
  let result = '';
  if (angle === 360 || angle < 30) {
    hours = '12';
  }
  if (hours >=10) {
    hours = hours.toString();
  } else {
    hours = '0' + hours.toString();
  }
  if (minutes >= 10) {
    minutes = minutes.toString();
  } else {
     minutes = '0' + minutes.toString();
  }
  result = hours + ':' + minutes;
  return result;
}
```