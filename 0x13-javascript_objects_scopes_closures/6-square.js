#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; i < this.width; j++) {
        str += c || 'X';
      }
      console.log(str);
    }
  }
};
