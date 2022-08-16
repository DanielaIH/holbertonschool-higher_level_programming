#!/usr/bin/node
const args = process.argv;
if (args.length < 4) {
  console.log(0);
} else {
  const numbers = args.slice(2).map(Number);
  numbers.sort(function (a, b) { return a - b; });
  console.log(numbers[numbers.length - 2]);
}
