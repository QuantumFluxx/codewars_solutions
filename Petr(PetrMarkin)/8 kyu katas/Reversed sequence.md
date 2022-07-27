## Description:

Build a function that returns an array of integers from n to 1 where n>0.

### Examples (input --> output):
```
n=5 --> [5,4,3,2,1]
```

 ## Solution:
 
```javascript
const reverseSeq = n => {
let arr = [];
  for (let i=n; i>0; i--) {
    arr.push(i);
    } return arr;
};
```