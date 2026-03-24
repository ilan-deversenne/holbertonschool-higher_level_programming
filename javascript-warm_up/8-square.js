#!/usr/bin/node

let str = '';
const n = parseInt(process.argv[2]);
if (n) {
    for(let x = 0; x < n; x++) {
        for (let y = 0; y < n; y++) {
            str += 'X';
        }
        if (x < n - 1) str += '\n';
    }
    console.log(str);
}else {
    console.log('Missing size');
}
