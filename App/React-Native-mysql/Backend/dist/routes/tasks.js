"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;
var _express = require("express");
var _tasks = require("../controllers/tasks");
var router = (0, _express.Router)();
router.get('/tasks', _tasks.getTasks);
router.get('/tasks/:count', _tasks.getTasksCount);
router.get('/tasks/:id', _tasks.getTask);
router.post('/tasks', _tasks.createTasks);
router["delete"]('/tasks/:id', _tasks.deleateTasks);
router.put('/tasks/:id', _tasks.updateTasks);
var _default = exports["default"] = router;