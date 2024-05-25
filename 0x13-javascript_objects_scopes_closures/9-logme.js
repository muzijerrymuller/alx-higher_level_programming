#!/usr/bin/node
let logCount = 0;

exports.logMe = (item) => {
  console.log(`${logCount}: ${item}`);
  logCount++;
};
