#!/usr/bin/node
const args = process.argv;
let counter = 0;
if (isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else {
  while (counter < parseInt(args[2])) {
    console.log('C is fun');
    counter++;
  }
}
