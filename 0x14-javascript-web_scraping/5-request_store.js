#!/usr/bin/node

const fs = require('fs');
const { get } = require('http');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Usage: ./script.js <URL> <file_path>');
  process.exit(1);
}

get(url, (response) => {
  const fileStream = fs.createWriteStream(filePath);
  response.pipe(fileStream);

  fileStream.on('finish', () => {
    fileStream.close(() => {
      console.log('File written successfully');
    });
  });
}).on('error', (err) => {
  console.error(`Error: ${err.message}`);
}); 
