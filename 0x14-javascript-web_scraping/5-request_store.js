#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const fs = require('fs');
request(url, 'utf-8').pipe(fs.createWriteStream(process.argv[3]));
