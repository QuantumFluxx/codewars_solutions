## Description:

Write a function that takes a string and outputs a strings of 1's and 0's where vowels become 1's and non-vowels become 0's.

All non-vowels including non alpha characters (spaces,commas etc.) should be included.

### Examples (input --> output):
```
vowelOne( "abceios" ) // "1001110"

vowelOne( "aeiou, abc" ) // "1111100100"
```

 ## Solution:
 
```javascript
function vowelOne(s){
  let result = s.replace(/./g,v=>/[aeiou]/i.test(v) ? '1':'0')
  return result
}
```