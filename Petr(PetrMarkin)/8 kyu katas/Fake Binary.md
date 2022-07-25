## Description:

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string

 ## Solution:
 
```javascript
function fakeBin(x){
  return x.replace(/0|1|2|3|4/g, 0).replace(/5|6|7|8|9/g, 1);
}
```