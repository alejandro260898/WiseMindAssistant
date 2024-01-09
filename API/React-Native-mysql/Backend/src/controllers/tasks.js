import {connect} from '../database'

export const getTasks = async(req,res) => {
    const db = await connect();

    const[rows]=await db.query('SELECT * FROM users.usuarios');

    //const [rows]= await connect.query('SELECT * FROM users.usuarios')
    console.log(rows);

    res.json(rows)
}

export const getTask =(req,res) => {
    res.send('Hello World')
}
export const createTasks =(req,res) => {
    res.send('Hello World')
}
export const deleateTasks =(req,res) => {
    res.send('Hello World')
}
export const updateTasks =(req,res) => {
    res.send('Hello World')
}
export const getTasksCount =(req,res) => {
    res.send('Hello World')
}