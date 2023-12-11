#!/usr/bin/node
function callMeMoby (x, TheFunction) {
  for (let i = 0; i < x; i++) {
    TheFunction();
  }
}
module.exports = { callMeMoby };
