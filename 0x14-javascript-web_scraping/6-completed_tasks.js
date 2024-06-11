#!/usr/bin/node
// Number of tasks completed by user id.

const args = process.argv;
const reqURL = args[2];
const request = require('request');

request(reqURL, (error, response, body) => {
  if (error) {
    console.log('Error:', error);
  } else {
    const todos = JSON.parse(body);
    const taskCount = {};

    todos.forEach(todo => {
      if (todo.completed) {
        const userId = todo.userId.toString();
        if (taskCount[userId]) {
          taskCount[userId]++;
        } else {
          taskCount[userId] = 1;
        }
      }
    });

    console.log(taskCount);
  }
});
