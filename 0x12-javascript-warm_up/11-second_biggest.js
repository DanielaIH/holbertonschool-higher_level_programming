#!/usr/bin/node
const args = process.argv;
if (args.length < 4) {
  console.log(0);
} else {
  const numbers = args.map(Number);
  numbers.sort().reverse();
  let i = 0;
  while (isNaN(numbers[i])) { i++; }
  console.log(numbers[i + 1]);
}
