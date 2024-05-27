#!/usr/bin/node

const fs = require('fs');
const http = require('http');
const https = require('https');
const url = require('url');

const inputUrl = process.argv[2];
const filePath = process.argv[3];

if (!inputUrl || !filePath) {
  console.error('Usage: ./script.js <URL> <file_path>');
  process.exit(1);
}

const parsedUrl = url.parse(inputUrl);
const protocol = parsedUrl.protocol === 'https:' ? https : http;

const request = protocol.get(inputUrl, (response) => {
  if (response.statusCode >= 300 && response.statusCode < 400 && response.headers.location) {
    const redirectUrl = response.headers.location;
    console.log(`Redirecting to ${redirectUrl}`);
    const redirectProtocol = redirectUrl.startsWith('https') ? https : http;
    redirectProtocol.get(redirectUrl, (res) => {
      res.pipe(fs.createWriteStream(filePath));
    });
  } else if (response.statusCode === 200) {
    response.pipe(fs.createWriteStream(filePath));
  } else {
    console.error(`Failed to get '${inputUrl}' (${response.statusCode})`);
  }
}).on('error', (err) => {
  console.error(`Error: ${err.message}`);
});
