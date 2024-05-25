#!/usr/bin/node
const counter = {
  logCount: 0,
  logMe(item) {
    console.log(`${this.logCount}: ${item}`);
    this.logCount++;
  }
};

exports.logMe = function (item) {
  counter.logMe(item);
};
