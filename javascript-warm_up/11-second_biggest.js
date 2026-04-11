#!/usr/bin/node
console.log(process.argv.slice(2).sort().reverse()[1] || 0)
