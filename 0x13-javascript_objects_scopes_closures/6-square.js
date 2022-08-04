#!/usr/bin/node
// Class Square that inherits from rectangle

class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i;
    for (i = 0; i < this.height; i++) {
      console.log(c.repeat(this.height));
    }
  }
}

module.exports = Square;
