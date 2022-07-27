## Description:

You get an array of numbers, return the sum of all of the positives ones.

### Examples (input --> output):
```
[1,-4,7,12] => 1 + 7 + 12 = 20
```

 ## Solution:
 
```javascript
function positiveSum(arr) {
let count = 0;
  for (let i = 0; i < arr.length; i++){
    if(arr[i] > 0) count+= arr[i];
  }
  return count;
}
```