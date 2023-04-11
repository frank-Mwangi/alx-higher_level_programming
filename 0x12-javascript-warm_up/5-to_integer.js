#!/usr/bin/node
const myVar = process.argv.slice(2);
let x = parseInt(myVar[0]);

if (isNaN(x)) {
  x = 'Not a number';
} else {
  x = 'My number: ' + x;
}
console.log(x);
