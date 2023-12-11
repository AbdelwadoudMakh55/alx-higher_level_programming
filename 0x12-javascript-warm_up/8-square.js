#!/usr/bin/node
if (process.argv[2]) {
  if (isNaN(process.argv[2]) === false) {
    for (let i = 0; i < Number(process.argv[2]); i++) {
      console.log('X'.repeat(Number(process.argv[2])));
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
