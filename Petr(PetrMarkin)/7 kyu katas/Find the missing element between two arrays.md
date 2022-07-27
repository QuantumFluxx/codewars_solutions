## Description:

Given two integer arrays where the second array is a shuffled duplicate of the first array with one element missing, find the missing element.

Please note, there may be duplicates in the arrays, so checking if a numerical value exists in one and not the other is not a valid solution.

The first array will always have at least one element.

### Examples (input --> output):
```
find_missing([1, 2, 2, 3], [1, 2, 3]) => 2

find_missing([6, 1, 3, 6, 8, 2], [3, 6, 6, 1, 2]) => 8
```

 ## Solution:
 
```javascript
function findMissing(arr1, arr2) {
  let index;
  for(let i = 0; i < arr1.length; i++){
    index = arr2.indexOf(arr1[i]);
    if(index > -1){
      arr2.splice(index, 1);
    } else {
    return arr1[i];
    }
  }
}
```