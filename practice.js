let arr = [
  [1, 2],
  [2, 2],
  [2, 1]
];
const xmap = new Map();
const ymap = new Map();
let answer = [];
for (let [x, y] of arr) {
  if (xmap.has(x)) {
    xmap.set(x, xmap.get(x) + 1);
  } else {
    xmap.set(x, 1);
  }
  if (y in ymap) {
    ymap[y] += 1;
  } else {
    ymap[y] = 1;
  }
}
for (let [key, val] of xmap) {
  if (val === 1) {
    answer.push(key);
  }
}
console.log(answer);
