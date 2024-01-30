#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const charList = JSON.parse(body).characters;
  for (let i = 0; i < charList.length; i++) {
    request(charList[i], function (error, response, body) {
      if (error) {
        console.error(error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
