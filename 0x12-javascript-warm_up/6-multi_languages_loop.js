#!/usr/bin/node

const myVar = ['C is fun', 'Python is cool', 'Javascript is amazing'];
let args = 0;

for (args in myVar) {
  console.log(myVar[args]);
}
