#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let counter = 0;
    while (counter < this.height) {
      console.log(c.repeat(this.width));
      counter++;
    }
  }
}

module.exports = Square;
