## Description:

This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.


 ## Solution:
 
```javascript
function simpleMultiplication(number) {
  let odd = number * 8;
  let even = number * 9
    return (number % 2 === 0 ? odd : even);
}
```