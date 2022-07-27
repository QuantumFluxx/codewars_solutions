## Description:

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

 ## Solution:
 
```javascript
function isPangram(string){
  let arr = [];
  let n = string.toLowerCase();
  let str = n.replace(/[^a-zа-я]+/g, '');
  for (let i = 0;i < str.length; i++) {
    if (!arr.includes(str[i])) {
      arr.push(str[i]);
    }
  }
  if (arr.length === 26) {
    return true;
  } else {
    return false;
  }
}
```