#!/usr/bin/node

const line = process.argv;

if (line.length < 3) {
  console.log('No argument');
} else if (line.length > 3) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
