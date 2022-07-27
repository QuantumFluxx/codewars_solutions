## Description:

Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

### Examples (input --> output):
```
uniqueInOrder('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
uniqueInOrder('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
uniqueInOrder([1,2,2,3,3])       == [1,2,3]
```

 ## Solution:
 
```javascript
var uniqueInOrder=function(iterable){
  let arr = []
  for (let i = 0; i < iterable.length; i++) {
    if (iterable[i] != iterable[i-1]) {
      arr.push(iterable[i])
    }
  }
  return arr
}
```