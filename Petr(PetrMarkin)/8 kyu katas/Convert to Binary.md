## Description:

Task Overview
Given a non-negative integer n, write a function to_binary/ToBinary which returns that number in a binary format.
```
to_binary(1)  /* should return 1 */
to_binary(5)  /* should return 101 */
to_binary(11) /* should return 1011 */
```

### Examples (input --> output):
```
toBinary(1)  /* should return 1 */
toBinary(5)  /* should return 101 */
toBinary(11) /* should return 1011 */
```

 ## Solution:
 
```javascript
function toBinary(n){
  return parseInt(n.toString(2));
}
```