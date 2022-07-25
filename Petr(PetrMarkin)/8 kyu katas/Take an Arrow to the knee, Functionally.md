## Description:

Come here to practice the Arrow style functions Not much else to say good luck!
Details
You will be given an array of numbers which can be used using the String.fromCharCode() (JS), Tools.FromCharCode() (C#) method to convert the number to a character. It is recommended to map over the array of numbers and convert each number to the corresponding ascii character.

### Examples (input --> output):
```
These are example of how to convert a number to an ascii Character:
Javascript => String.fromCharCode(97) // a
C# => Tools.FromCharCode(97) // a
```

 ## Solution:
 
```javascript
var ArrowFunc = function(arr) {
  let i = 0;
  let result = '';
  for (let i = arr.length -1; i >= 0; i -= 1) {
    result = `${String.fromCharCode(arr[i])}${result}`;
  }
  return result;
}
```