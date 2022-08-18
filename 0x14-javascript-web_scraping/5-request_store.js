#!/usr/bin/node
const axios = require('axios').default;
const fs = require('fs');
const args = process.argv;
axios.get(args[2])
  .then(function (response) {
    const reading = response.data;
    fs.writeFile(args[3], reading, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  })
  .catch(function (error) {
    console.log(error);
  });
