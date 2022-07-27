## Description:

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

 ## Solution:
 
```javascript
function findShort(s){
  let arr = s.split(' ');
  let arr1 = [];
  arr.forEach((item) => {
    item = item.length;
    arr1.push(item)
  })

  arr1.sort( (a, b) => a - b );
  console.log(arr1)
  return arr1[0]
}
```