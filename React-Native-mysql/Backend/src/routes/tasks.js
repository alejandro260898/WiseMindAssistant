import {Router} from 'express';
import {createTasks, deleateTasks, getTask, getTasks, getTasksCount, updateTasks} from '../controllers/tasks';
const router = Router();
router.get('/tasks',getTasks)
router.get('/tasks/:count',getTasksCount)
router.get('/tasks/:id',getTask)
router.post('/tasks',createTasks)

router.delete('/tasks/:id',deleateTasks)

router.put('/tasks/:id',updateTasks)
export default router