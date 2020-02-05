#!/usr/bin/node

if (isNaN(process.argv[2]) === true) {
  console.log(1);
} else {
  console.log(factorial(parseInt(process.argv[2])));
}

function factorial (n) {
  if ((n === 0) || (n === 1)) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}
