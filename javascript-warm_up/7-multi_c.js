#!/usr/bin/node

const n = parseInt(process.argv[2]);
for (let i = 0; i < n; i++) {
  console.log('C is fun');
}
if (!process.argv[2] || !n) console.log('Missing number of occurrences');
