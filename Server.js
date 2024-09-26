const express = require('express');
const mysql = require('mysql');
const cors = require('cors');

const app = express();
const port = 3301;

const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'users',
  port: 3307,
});

db.connect((err) => {
  if (err) {
    console.error('Error al conectar a la base de datos:', err);
  } else {
    console.log('conexion bien');
  }
});

const corsOptions = {
  origin: '*',
  methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
  credentials: true,
  optionsSuccessStatus: 204,
};

app.use(cors(corsOptions));
app.use(express.json());

app.get('/usuarios', (req, res) => {
    
  const sql = 'SELECT * FROM nuevoUsuario';
  console.log(sql)

  db.query(sql, (err, result) => {

    if (err) {
      console.error('Error al ejecutar la consulta SQL:', err);
      res.status(500).json({ error: 'Error interno del servidor' });
    } else {
      if (result.length > 0) {
        res.status(200).json(result);
      } else {
        res.status(200).json([]);
      }
    }
  });
});


app.listen(port, () => {
  console.log(`Servidor escuchando en http://localhost:${port}`);
});
