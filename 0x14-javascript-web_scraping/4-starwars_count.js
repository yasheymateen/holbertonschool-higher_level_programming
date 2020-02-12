#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      for (let char = 0; char < results[i].characters.length; char++) {
        if (results[i].characters[char].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
