#!/usr/bin/node
// prints star wars title according to spacific integer

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
