#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const result = JSON.parse(body);
    const dict = {};
    for (let i = 0; i < result.length; i++) {
      if (result[i].completed === true) {
        if (dict[result[i].userId] === undefined) {
          dict[result[i].userId] = 1;
        } else {
          dict[result[i].userId] += 1;
        }
      }
    }
    console.log(dict);
  }
});
