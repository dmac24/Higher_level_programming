#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const destination = process.argv[3];

request(url, function (err, response, body) {
  if (err) console.log(err);
  else {
    fs.writeFile(destination, body, 'utf-8', (err) => {
      if (err) console.log(err);
    });
  }
});
