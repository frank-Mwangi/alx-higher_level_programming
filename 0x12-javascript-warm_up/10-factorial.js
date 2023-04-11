#!/usr/bin/node
const myVar = process.argv.slice(2);
const x = parseInt(myVar[0]);
function factorial (i) {
  if (i === 0) {
    return 1;
  } else {
    return i * factorial(i - 1);
  }
}
if (isNaN(x)) {
  console.log(1);
} else {
  console.log(factorial(x));
}
