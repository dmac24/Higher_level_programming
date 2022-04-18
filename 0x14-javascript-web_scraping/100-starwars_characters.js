#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

const syncChars = ([firstUrl, ...characters]) => {
  if (!firstUrl) {
    return;
  }
  request(firstUrl, function (err, _, body) {
    if (err) console.log(err);
    else {
      const { name } = JSON.parse(body);
      console.log(name);
    }
    syncChars(characters);
  });
};

request(`${url}${movieId}`, function (err, _, body) {
  if (err) console.log(err);
  else {
    const { characters } = JSON.parse(body);
    syncChars(characters);
  }
});
