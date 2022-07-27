## Description:

Given an array/list [] of n integers , find maximum triplet sum in the array Without duplications.

Array/list size is at least 3 .

Array/list numbers could be a mixture of positives , negatives and zeros .

Repetition of numbers in the array/list could occur , So (duplications are not included when summing).

### Examples (input --> output):
```
1- maxTriSum ({3,2,6,8,2,3}) ==> return (17)
```

 ## Solution:
 
```javascript
function maxTriSum(numbers){
  let arr = [...new Set(numbers)];
  let numMax1 = Math.max(...arr);
  let newArray = arr.filter(function(f) { return f !== numMax1 });
  let numMax2 = Math.max(...newArray);
  let newArray2 = newArray.filter(function(f) { return f !== numMax2});
  let numMax3 = Math.max(...newArray2);
  let result = Number(numMax1)+ Number(numMax2) + Number(numMax3);
  return result;
}
```