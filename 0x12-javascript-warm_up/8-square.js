#!/usr/bin/node

const line = process.argv[2];

if (isNaN(line)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < line; i++) {
    console.log('X'.repeat(line));
  }
}
