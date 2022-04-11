#!/usr/bin/node

const process = require('process');
const args = process.argv;
const numbers = [];

for (let i = 2; i < args.length; i++) {
  numbers.push(parseInt(args[i]));
}

numbers.splice(numbers.indexOf(Math.max(...numbers)), 1);

if (numbers.length === 0) {
  console.log(0);
} else {
  console.log(Math.max(...numbers));
}
