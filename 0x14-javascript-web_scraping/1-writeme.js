#!/usr/bin/node
// this code writes a string to a file
// The content of the file must be written in utf-8
// If an error occurred during while writing, print the error object

const fs = require('fs');
const file = process.argv[2];
const write_ = process.argv[3];

fs.writeFile(file, write_, 'utf-8', function (error) {
  if (error) {
    console.log(error);
  }
});
