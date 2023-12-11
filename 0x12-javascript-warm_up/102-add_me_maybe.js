#!/usr/bin/node
function addMeMaybe (number, TheFunction) {
  TheFunction(number + 1);
}
module.exports = { addMeMaybe };
