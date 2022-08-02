#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments

const args = process.argv;
const nextMax = args.length;
if (nextMax > 3) {
  args.sort();
  console.log(args[nextMax - 2]);
} else {
  console.log(0);
}
