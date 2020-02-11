#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/';
const id = process.argv[2];

request(url + id, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
