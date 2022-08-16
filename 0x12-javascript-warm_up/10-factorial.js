#!/usr/bin/node
const args = process.argv;
if (isNaN(args[2])) {
  console.log(1);
} else {
  const number = parseInt(args[2]);
  console.log(factorial(number));
}
function factorial (number) {
  if (number === 0) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}
