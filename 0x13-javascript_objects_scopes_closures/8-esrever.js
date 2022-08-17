#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;
  const reversedArray = [];
  let i = 1;

  while (len >= i) {
    reversedArray.push(list[len - i++]);
  }
  return reversedArray;
};
