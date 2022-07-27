## Description:

Some people have been killed!
You have managed to narrow the suspects down to just a few. Luckily, you know every person who those suspects have seen on the day of the murders.

Task.
Given a dictionary with all the names of the suspects and everyone that they have seen on that day which may look like this:

### Examples (input --> output):
```
{'James': ['Jacob', 'Bill', 'Lucas'],
 'Johnny': ['David', 'Kyle', 'Lucas'],
 'Peter': ['Lucy', 'Kyle']}
and dead people:
['Lucas', 'Bill']
```

 ## Solution:
 
```javascript
function killer(suspectInfo, dead) {
    let killerName = ''
    let maxDead = 0
    for ([name, personMet] of Object.entries(suspectInfo)) {
        let count = 0
        dead.forEach(victim => {
            count = (personMet.includes(victim)) ? count + 1 : count
        });
        if (count > maxDead) {
            maxDead = count
            killerName = name
        }
    }
  return killerName
}
```