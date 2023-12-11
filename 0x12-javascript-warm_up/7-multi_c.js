#!/usr/bin/node
const sentence = 'C is fun';
if (process.argv[2]) {
  if (isNaN(process.argv[2]) === false) {
    for (let i = 0; i < Number(process.argv[2]); i++) {
      console.log(sentence);
    }
  }
} else {
  console.log('Missing number of occurrences');
}
