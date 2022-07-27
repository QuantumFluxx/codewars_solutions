## Description:

Given a string s. You have to return another string such that even-indexed and odd-indexed characters of s are grouped and groups are space-separated (see sample below)

Even indices 0, 2, 4, 6, so we have 'CdWr' as the first group
odd ones are 1, 3, 5, 7, so the second group is 'oeas'
And the final string to return is 'Cdwr oeas'


### Examples (input --> output):
```
S[0] = 'C'
S[1] = 'o'
S[2] = 'd'
S[3] = 'e'
S[4] = 'W'
S[5] = 'a'
S[6] = 'r'
S[7] = 's'
```

 ## Solution:
 
```javascript
function sortMyString(S) {
let str1 = '';
let str2 = '';
  for (let i = 0; i < S.length; i++) {
    if (i % 2 === 0 || i === 0) {
      str1 += S[i];
    } else {
      str2 += S[i];
    };
  }
  return str1 + ' ' + str2; 
}
```