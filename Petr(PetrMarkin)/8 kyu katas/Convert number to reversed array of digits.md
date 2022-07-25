## Description:

Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

### Examples (input --> output):
```
348597 => [7,9,5,8,4,3]
0 => [0]
```

 ## Solution:
 
```javascript
function digitize(n) {
  let str = n.toString();
  let arr = [];
  for (let i = 0; i < str.length; i++) {
    arr.push(Number(str[i]))
  }
  return arr.reverse()
}
```