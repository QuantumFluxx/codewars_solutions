## Description:

Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

### Examples (input --> output):
```
[true,  true,  true,  false,
  true,  true,  true,  true ,
  true,  false, true,  false,
  true,  false, false, true ,
  true,  true,  true,  true ,
  false, false, true,  true]
```
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined


 ## Solution:
 
```javascript
function countSheeps(arrayOfSheep) {
  let counter = 0;

for (let elem of arrayOfSheep) {
  if (elem == true) {
    counter++;
  }
}
  return counter;
}
```