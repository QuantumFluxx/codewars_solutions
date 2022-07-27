## Description:

Complete the solution so that the function will break up camel casing, using a space between words.

### Examples (input --> output):
```
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
```

 ## Solution:
 
```javascript
function solution(str) {
  let output = ''
  for (let i = 0; i < str.length;i++) {
    if (str[i] === 'A' || str[i] === 'B' || str[i] === 'C' || str[i] === 'D' || str[i] === 'E' || str[i] === 'F' ||
       str[i] === 'G' || str[i] === 'H' || str[i] === 'I' || str[i] === 'J' || str[i] === 'K' || str[i] === 'L' ||
       str[i] === 'M' || str[i] === 'N' || str[i] === 'O' || str[i] === 'P' || str[i] === 'R' || str[i] === 'S' ||
       str[i] === 'Q' || str[i] === 'T' || str[i] === 'U' || str[i] === 'V' || str[i] === 'W' || str[i] === 'X' ||
       str[i] === 'Y' || str[i] === 'Z') {
      output += ' ' + str[i];
    }
    else {
      output += str[i];
    }
  }
  return output
}
```