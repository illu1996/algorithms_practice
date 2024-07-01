let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let n = input[0];
let map = [];

for (let i = 1; i < input.length; i++) {
  let row = input[i].split('').map(Number);
  map.push(row);
}

console.log(map);
