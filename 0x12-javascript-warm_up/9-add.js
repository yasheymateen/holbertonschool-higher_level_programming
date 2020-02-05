#!/usr/bin/node

if (!process.argv[2] || !process.argv[3]) {
  console.log('NaN');
} else {
  console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
}

function add (a, b) {
  return (a + b);
}
