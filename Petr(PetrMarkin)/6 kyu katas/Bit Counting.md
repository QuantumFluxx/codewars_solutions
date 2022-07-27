## Description:

Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

### Examples (input --> output):
```
The binary representation of 1234 is 10011010010, so the function should return 5 in this case
```

 ## Solution:
 
```javascript
var countBits = function(n) {
  let binary = (n).toString(2);
  let result = 0;
  for (let i = 0; i < binary.length; i++) {
    if (binary[i] === '1') {
      result += 1;
    }
    if (binary[i] === '0') {
      result += 0;
    }
  }
  return result;
};
```