## Description:

Write a function that returns only the decimal part of the given number.

You only have to handle valid numbers, not Infinity, NaN, or similar. Always return a positive decimal part.

### Examples (input --> output):
```
getDecimal(2.4)  === 0.4
getDecimal(-0.2) === 0.2
```

 ## Solution:
 
```javascript
function getDecimal(n){
  let result = '';
  if (n % 1 === 0) {
    return 0;
} else {
  n = n % 1;
  if (n < 0) {
    n = n.toString().slice(1);
    return Number(n);
  } else {
    return n;
  }
}
}
```