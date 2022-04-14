#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const aux = {};
    const json = JSON.parse(body);
    for (let j = 0; j < json.length; j++) {
      if (json[j].completed === true) {
        if (aux[json[j].userId] === undefined) {
          aux[json[j].userId] = 0;
        }
        aux[json[j].userId]++;
      }
    }
    console.log(aux);
  }
});
