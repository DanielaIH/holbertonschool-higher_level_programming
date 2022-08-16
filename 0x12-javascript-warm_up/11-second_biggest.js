#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (args.length < 4) {
  console.log(0);
} else {
  const numbers = args.slice(2).map(Number);
  numbers.sort();
  console.log(numbers[numbers.length - 2]);
}
