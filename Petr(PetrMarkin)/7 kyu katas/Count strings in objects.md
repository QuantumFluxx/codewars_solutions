## Description:

Create a function strCount (takes an object as argument) that will count all string values inside an object.

### Examples (input --> output):
```
strCount({
  first: "1",
  second: "2",
  third: false,
  fourth: ["anytime",2,3,4],
  fifth:  null
  })
  //returns 3
```

 ## Solution:
 
```javascript
function strCount(obj){
  let res = 0;
  
  for (let key in obj) {
    if (typeof(obj[key]) === 'string') {
      res += 1;
    }
    if (typeof(obj[key]) === 'object') {
      res += strCount(obj[key]);
    }
  }
  return res;
}
```