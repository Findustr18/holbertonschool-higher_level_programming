#!/usr/bin/node
// script that computes and prints a factorial

console.log(factorial(parseInt(process.argv[2])));
function factorial (f) {
  if (f) {
    return (f * factorial(f - 1));
  } else {
    return 1;
  }
}
