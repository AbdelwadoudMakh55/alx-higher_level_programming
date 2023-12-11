#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
if (process.argv[2]) {
  if (process.argv[3]) {
    add(Number(process.argv[2]), Number(process.argv[3]));
  } else {
    console.log(NaN);
  }
} else {
  console.log(NaN);
}
