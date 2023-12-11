#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) === true || n === 0 || n === 1) {
    return 1;
  } else {
    return factorial(n - 1) * n;
  }
}
if (process.argv[2]) {
  console.log(factorial(Number(process.argv[2])));
} else {
  console.log(factorial(NaN));
}
