#!/usr/bin/node
const axios = require('axios').default;
const args = process.argv;
axios.get(args[2])
  .then(function (response) {
    console.log('code: ' + response.status);
  })
  .catch(function (error) {
    console.log('code: ' + error.response.status);
  });
