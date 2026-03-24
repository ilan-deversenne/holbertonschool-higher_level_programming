#!/usr/bin/node

const n = parseInt(process.argv[2]);

function factorial (n) {
  if (!n || n == 1) return 1;
  if (n < 1) return -1;

  return n * factorial(n - 1);
}

console.log(factorial(n));
