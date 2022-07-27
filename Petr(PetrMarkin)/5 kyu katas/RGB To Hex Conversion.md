## Description:

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

### Examples (input --> output):
```
rgb(255, 255, 255) // returns FFFFFF
rgb(255, 255, 300) // returns FFFFFF
rgb(0,0,0) // returns 000000
rgb(148, 0, 211) // returns 9400D3
```

 ## Solution:
 
```javascript
function rgb(r, g, b){
  let red = '';
  let blue = '';
  let green = '';
  if (r < 1) {
    red = '00';
  } else if (r > 255) {
  red = 'FF';
}else {
    red = r.toString(16);
  }
  if (g < 1) {
    green = '00';
  } else if (g > 255) {
  green = 'FF';
}else {
    green = g.toString(16);
  }
  if (b < 1) {
    blue = '00';
  }else if (b > 255) {
  blue = 'FF';
} else {
    blue = b.toString(16);
  }
  if (red.length === 1) {
    red = 0 + red;
  }
  if (green.length ===  1) {
    green = 0 + green;
  }
  if (blue.length ===  1) {
    blue = 0 + blue;
  }
  let res = red + green + blue;
  return res.toUpperCase();
}
```