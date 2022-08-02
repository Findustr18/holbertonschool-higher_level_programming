#!/usr/bin/node
// script that prints x times “C is fun”

const x = parseInt(process.argv[2]);
if (x) {
  const phrase = ['C is fun'];
  for (let i = 0; i < x; i++) {
    console.log(phrase[0]);
  }
} else {
  console.log('Missing number of occurrences');
}
