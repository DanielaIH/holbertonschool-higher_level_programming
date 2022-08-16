#!/usr/bin/node
const args = process.argv;
if (args.length < 4) {
  console.log(0);
} else {
  const arrayOfNumbers = args.map(Number);
  arrayOfNumbers.sort().reverse();
  console.log(arrayOfNumbers[3]);
}
