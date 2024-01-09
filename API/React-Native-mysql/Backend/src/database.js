import mysql from 'mysql2/promise'
import { config } from "C:/Users/raufa/OneDrive/Escritorio/React-Native-mysql/Backend/src/.config.js";



export const connect = async() =>{
    //const conn = await mysql.createConnection(config);
     return await mysql.createConnection(config);
    //const [rows]= await conn.query("SELECT 1+1" );
   // console.log(rows)
};
