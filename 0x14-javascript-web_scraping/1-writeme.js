#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const content = process.argv[3];

fs.writefile(file, content, function (err) {
  if (err) {
    console.log(err);
  }
});
