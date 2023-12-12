#!/usr/bin/node
function esrever (list) {
  const rever = [];
  for (let i = 0; i < list.length; i++) {
    rever[i] = list[list.length - 1 - i];
  }
  return rever;
}
module.exports = { esrever };
