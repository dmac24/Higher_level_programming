#!/usr/bin/node

const request = require('request');
const interador = process.argv[2];
request(interador, function (error, response, list) {
  if (!error) {
    const results = JSON.parse(list).results;
    console.log(results.reduce((cont, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? cont + 1
        : cont;
    }, 0));
  }
});
