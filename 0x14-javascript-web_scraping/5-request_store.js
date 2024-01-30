#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  fs.writeFile(process.argv[3], body, function (err) {
    if (err) {
      console.error(err);
    }
  });
});
