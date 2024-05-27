#!/usr/bin/node

const axios = require('axios');
const targetUrl = process.argv[2];

if (!targetUrl) {
  console.error('Usage: ./status_code.js <URL>');
  process.exit(1);
}

axios.get(targetUrl, { maxRedirects: 10 })
  .then(response => {
    console.log(`code: ${response.status}`);
  })
  .catch(error => {
    if (error.response) {
      console.log(`code: ${error.response.status}`);
    } else {
      console.error('Error:', error.message);
    }
  });
