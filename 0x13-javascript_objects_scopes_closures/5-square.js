#!/usr/bin/node
// Class Square that inherits from rectangle

class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
