#!/usr/bin/node
const array = [];
let j = 0;
if (process.argv[2]) {
  if (process.argv.length === 3) {
    console.log(0);
  } else {
    for (let i = 2; i < process.argv.length; i++) {
      array[j] = Number(process.argv[i]);
      j++;
    }
    array.splice(array.indexOf(Math.max(...array)), 1);
    console.log(Math.max(...array));
  }
} else {
  console.log(0);
}
