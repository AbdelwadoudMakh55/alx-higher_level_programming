#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  const todos = JSON.parse(body);
  const todosByuser = {};
  for (let i = 1; i < 11; i++) {
    todosByuser[i] = 0;
  }
  for (let j = 0; j < todos.length; j++) {
    if (todos[j].completed === true) {
      todosByuser[todos[j].userId]++;
    }
  }
  console.log(todosByuser);
});
