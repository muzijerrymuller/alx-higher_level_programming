#!/usr/bin/node
const http = require('http');
const https = require('https');
const url = require('url');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (!movieId) {
  console.error('Usage: ./starwars_movie.js <movie_id>');
  process.exit(1);
}

const parsedUrl = url.parse(apiUrl);
const protocol = parsedUrl.protocol === 'https:' ? https : http;

protocol.get(apiUrl, (response) => {
  let data = '';

  response.on('data', (chunk) => {
    data += chunk;
  });

  response.on('end', () => {
    if (response.statusCode === 200) {
      const movie = JSON.parse(data);
      console.log(movie.title);
    } else {
      console.log(`Error: ${response.statusCode}`);
    }
  });
}).on('error', (error) => {
  console.error('Error:', error.message);
});
