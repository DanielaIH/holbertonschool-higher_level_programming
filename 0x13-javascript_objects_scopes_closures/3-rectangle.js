#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let counter = 0;
    while (counter < this.height) {
      console.log('X'.repeat(this.width));
      counter++;
    }
  }
}
module.exports = Rectangle;
