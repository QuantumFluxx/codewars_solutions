## Description:

Task:
Your task is to write a function which returns the sum of following series upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
Rules:
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return 0.00

You will only be given Natural Numbers as arguments.

### Examples (input --> output):
```
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
```

 ## Solution:
 
```javascript
function SeriesSum(n)
{
  let b = 4;
  let sum = 1;
  if (n === 1) {
    return '1.00'
  }
  if (n === 0) {
    return '0.00'
  }
  for (let i = 1;i < n; i++, b+=3) {
    sum += 1/b;
  }
  console.log(b)
  return sum.toFixed(2)
}
```