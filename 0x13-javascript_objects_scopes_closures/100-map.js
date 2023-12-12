#!/usr/bin/node
const list1 = require('./100-data').list;
const map1 = list1.map((num, index) => num * index);
console.log(list1);
console.log(map1);
