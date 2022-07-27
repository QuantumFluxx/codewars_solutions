## Description:

Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer

 ## Solution:
 
```javascript
function squareDigits(num){
  num = num.toString();
  let result = ''
  let num1
  for (let i = 0;i < num.length; i++) {
     num1 = Number(num[i]);
     result += (num1**2);
  }
  return Number(result)
}
```