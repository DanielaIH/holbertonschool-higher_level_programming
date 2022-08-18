#!/usr/bin/node
const axios = require('axios').default;
const args = process.argv;
axios.get(args[2])
  .then(function (response) {
    const tasks = response.data;
    const completed_tasks = {};
    tasks.forEach((task) => {
      if (task.completed) {
        if (task.userId in completed_tasks) {
          completed_tasks[task.userId]++;
        } else {
          completed_tasks[task.userId] = 1;
        }
      }
    });
    console.log(completed_tasks);
  })
  .catch(function (error) {
    console.log(error);
  });
`const axios = require('axios').default;
const args = process.argv;
axios.get(args[2])
  .then(function (response) {
    const tasks = response.data;
    const count = tasks.filter(function (p) {
      return p.completed;
    });
    const users = count.groupBy(function (n) {
        return n.userId;
    })
    console.log(users);
  })
  .catch(function (error) {
    console.log(error);
  });
 `