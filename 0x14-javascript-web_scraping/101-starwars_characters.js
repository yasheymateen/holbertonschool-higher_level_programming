#!/usr/bin/node
const request = require('request');

let people = [];
const url = 'https://swapi.co/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    people = JSON.parse(body).characters;
    displayOrder(people, 0);
  }
});

function displayOrder (urls, i) {
  if (urls[i] !== undefined) {
    request(urls[i], function (err, response, body) {
      if (err) {
        console.log(err);
      } else {
        process.stdout.write(JSON.parse(body).name + '\n');
        displayOrder(urls, i + 1);
      }
    });
  }
}
