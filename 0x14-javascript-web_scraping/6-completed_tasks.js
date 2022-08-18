#!/usr/bin/node
const axios = require('axios').default;
const args = process.argv;
axios.get(args[2])
  .then(function (response) {
    const tasks = response.data;
    const completedtasks = {};
    tasks.forEach((task) => {
      if (task.completed) {
        if (task.userId in completedtasks) {
          completedtasks[task.userId]++;
        } else {
          completedtasks[task.userId] = 1;
        }
      }
    });
    console.log(completedtasks);
  })
  .catch(function (error) {
    console.log(error);
  });
