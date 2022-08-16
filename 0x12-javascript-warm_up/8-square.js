#!/usr/bin/node
const args = process.argv;
let counter = 0;
if (isNaN(args[2])) {
  console.log('Missing size');
} else {
  while (counter < parseInt(args[2])) {
    console.log('X'.repeat(args[2]));
    counter++;
  }
}
