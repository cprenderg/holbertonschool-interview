#!/usr/bin/node

/*
This program takes an argument to access the API of that film
then prints characters found in that film
*/

const request = require('request');
const endpoint = 'https://swapi-api.hbtn.io/api/films/';
const userInput = process.argv;

function getData (url) {
  /*
  Makes an api call to the url provided
  */
  return new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error) {
        reject(error);
        return;
      }
      resolve(JSON.parse(body));
    });
  });
}

async function printCharacters (url) {
  const data = await getData(url);
  for (const api of data.characters) {
    const character = await getData(api);
    console.log(character.name);
  }
}

getData(endpoint + userInput[2])
  .then(data => {
    printCharacters(data);
  })
  .catch(error => {
    console.error(error);
  });
