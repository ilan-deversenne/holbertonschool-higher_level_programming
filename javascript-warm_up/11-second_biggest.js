#!/usr/bin/node
console.log(process.argv.slice(2).map(Number).sort((a, b) => b - a)[1] || 0);
