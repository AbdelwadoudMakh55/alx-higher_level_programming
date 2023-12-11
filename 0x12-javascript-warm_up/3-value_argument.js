#!/usr/bin/node
const numArgs = process.argv.length;
if (numArgs === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
