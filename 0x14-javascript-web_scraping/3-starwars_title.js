#!/usr/bin/node

const got = require('got');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (!movieId) {
  console.error('Usage: ./starwars_movie.js <movie_id>');
  process.exit(1);
}

got(url)
  .then(response => {
    const movie = JSON.parse(response.body);
    console.log(movie.title);
  })
  catch(error => {
	if (error.response) {
		console.log(`Error: ${error.response.statusCode}`);
	} else {
		console.error('Error:', error.message);
	}
  });
