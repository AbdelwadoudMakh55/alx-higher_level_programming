#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  }
  const epList = JSON.parse(body).results;
  let charID18 = 0;
  for (let i = 0; i < epList.length; i++) {
    const chL = epList[i].characters;
    for (let j = 0; j < chL.length; j++) {
      if (chL[j].slice(43, chL[j].length - 1) === '18') {
        charID18++;
      }
    }
  }
  console.log(charID18);
});
