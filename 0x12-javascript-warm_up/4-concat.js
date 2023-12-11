#!/usr/bin/node
let printedString = 'undefined is undefined';
if (process.argv[2]) {
  printedString = process.argv[2] + ' is ';
  if (process.argv[3]) {
    printedString += process.argv[3];
  } else {
    printedString += 'undefined';
  }
  console.log(printedString);
} else {
  console.log(printedString);
}
