#!/usr/bin/node
let f1Content;
let f2Content;
const fs = require('fs');
fs.readFile(process.argv[2], function (err, data) {
  if (err) {
    console.error(err);
    return;
  }
  f1Content = data.toString();
  fs.writeFile(process.argv[4], f1Content, function (err) {
    if (err) {
      console.error(err);
    }
  });
});
fs.readFile(process.argv[3], function (err, data) {
  if (err) {
    console.error(err);
    return;
  }
  f2Content = data.toString();
  fs.appendFile(process.argv[4], f2Content, function (err) {
    if (err) {
      console.error(err);
    }
  });
});
