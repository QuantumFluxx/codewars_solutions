## Description:

I am the father of three wonderful sons. before the beginning of the school year, I promised them that I would buy a bicycle for someone who would bring the best marks at the end of the school year. it's time to keep promises and I count on you.

You have 3 input objects(school diaries) with school subjects and marks (1-10). 

### Examples (input --> output):
```
{
  'algebra': 6,
  'history': 8,
  'physics': 9,
  'geography': 2,
  'chemistry': 9
}
Return please :

'I need to buy a bicycle for my first son.' // the sum of the marks is the highest  in the first diary.

'I need to buy a bicycle for my second son.' // the sum of the marks is the highest in the second diary.

'I need to buy a bicycle for my third son.' //  the sum of the marks is the highest in the third diary.
```

 ## Solution:
 
```javascript
function whoseBicycle(diary1, diary2, diary3) {
  let arr = [Object.values(diary1),Object.values(diary2),Object.values(diary3)].map(v=>v.reduce((a,b)=>a+b,0))
  let index= arr.lastIndexOf(Math.max(...arr))
  return `I need to buy a bicycle for my ${index===0?'first':index===1?'second':'third'} son.`
}
```