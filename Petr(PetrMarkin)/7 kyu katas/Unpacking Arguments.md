## Description:

You must create a function, spread, that takes a function and a list of arguments to be applied to that function. You must make this function return the result of calling the given function/lambda with the given arguments.

### Examples (input --> output):
```
spread(someFunction, [1, true, "Foo", "bar"] ) 
// is the same as...
someFunction(1, true, "Foo", "bar")
```

 ## Solution:
 
```javascript
function spread(func, args) {
  let newFunc = (func(...args));
  return newFunc
}
```