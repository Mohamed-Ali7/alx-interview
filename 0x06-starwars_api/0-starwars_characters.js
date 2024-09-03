#!/usr/bin/node

const argv = require('process').argv;
const request = require('request');

const movieURL = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

request.get(movieURL, (err, res, body) => {
  if (err) {
    console.log(err);
  }

  const movie = JSON.parse(body);

  const charactersURL = movie.characters;
  const characterNames = [];

  for (const characterURL of charactersURL) {
    characterNames.push(new Promise((resolve, reject) => {
      request.get(characterURL, (characterErr, characterRes, characterBody) => {
        if (characterErr) {
          console.log(characterErr);
        }
        const character = JSON.parse(characterBody);
        resolve(character.name);
      });
    }));
  }

  Promise.all(characterNames).then((names) => {
    names.forEach(name => console.log(name));
  });
});
