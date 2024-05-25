#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    const width = this.width;
    const height = this.height;
    for (let i = 0; i < height; i++) {
      let s = '';
      for (let j = 0; j < width; j++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
