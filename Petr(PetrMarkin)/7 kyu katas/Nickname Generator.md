## Description:

Nickname Generator

Write a function, nicknameGenerator that takes a string name as an argument and returns the first 3 or 4 letters as a nickname.

If the 3rd letter is a consonant, return the first 3 letters.

If the 3rd letter is a vowel, return the first 4 letters.

If the string is less than 4 characters, return "Error: Name too short".

Notes:

Vowels are "aeiou", so discount the letter "y".
Input will always be a string.
Input will always have the first letter capitalised and the rest lowercase (e.g. Sam).
The input can be modified

### Examples (input --> output):
```
nickname("Robert") //=> "Rob"
nickname("Kimberly") //=> "Kim"
nickname("Samantha") //=> "Sam"
nickname("Jeannie") //=> "Jean"
nickname("Douglas") //=> "Doug"
nickname("Gregory") //=> "Greg"
```

 ## Solution:
 
```javascript
function nicknameGenerator(name){
  if (name.length < 4) {
    return 'Error: Name too short';
  } else if (name[2] === 'a' || name[2] === 'e' || name[2] === 'i' || name[2] === 'o' || name[2] === 'u') {
    return name.substring(4, 0);
  } else {
    return name.substring(3,0);
  }
}
```