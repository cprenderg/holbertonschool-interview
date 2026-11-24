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

getData(endpoint + userInput[2])
  .then(data => {
    for (const api of data.characters) {
      getData(api)
        .then(character => {
          console.log(character.name);
        })
        .catch(error => {
          console.error(error);
        });
    }
  })
  .catch(error => {
    console.error(error);
  });
