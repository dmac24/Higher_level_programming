#!/usr/bin/node

const line = process.argv[2];

if (isNaN(line)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + line);
}
