#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const epList = JSON.parse(body).results;
    let charID18 = 0;
    if (epList !== undefined) {
      for (let i = 0; i < epList.length; i++) {
        const chL = epList[i].characters;
        for (let j = 0; j < chL.length; j++) {
          if (chL[j].slice(43, chL[j].length - 1) === '18') {
            charID18++;
          }
        }
      }
    }
    console.log(charID18);
  }
});
