#!/usr/bin/node
const myVar = process.argv.slice(2);
if (myVar[0] === undefined) {
  myVar[0] = 'undefined';
} else if (myVar[1] === undefined) {
  myVar[1] = 'undefined';
}
console.log(myVar[0] + ' is ' + myVar[1]);
