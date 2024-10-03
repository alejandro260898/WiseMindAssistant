from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from app.chatbot.Vocabulario import Vocabulario
from app.chatbot.ChatBot import ChatBot

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://alex:1234@localhost/api_wise_mind_assistant'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    id =      db.Column(db.Integer, primary_key=True)
    nombre =  db.Column(db.String(255), nullable=True)
    api_key = db.Column(db.String(255), nullable=True)
    estatus = db.Column(db.String(10), nullable=False)

NOM_DATASET = './app/chatbot/data/dataset.xlsx'
COL_PREGUNTA = 'USUARIO'
COL_RESPUESTA = 'ASISTENTE'
EPOCAS = 800

modelo = None

@app.route('/')
def inicio():
    return 'Esta funcionando...'

@app.route('/pregunta', methods=['POST'])
def darPregunta():
    pregunta = request.get_json()
    pregunta = pregunta.get('message')
    palabras = modelo.predeccir(pregunta)
    respuesta = vocabulario.filtrarRespuesta(palabras=palabras)    
    return jsonify({ 
        'respuesta': respuesta 
    })

if __name__ == '__main__':
    vocabulario = Vocabulario()
    vocabulario.leerData(NOM_DATASET, COL_PREGUNTA, COL_RESPUESTA)
    vocabulario.cargar()

    preguntas = vocabulario.obtenerPreguntas()
    respuestas = vocabulario.obtenerRespuestas()
    preguntas_seq = vocabulario.crearSecuencias(preguntas)
    respuestas_seq = vocabulario.crearSecuencias(respuestas)
    tam_max_seq = vocabulario.crearTamMaxSecuencia(preguntas_seq + respuestas_seq)
    preguntas_seq = vocabulario.agregarPadding(preguntas_seq)
    respuestas_seq = vocabulario.agregarPadding(respuestas_seq)

    y = vocabulario.obtenerRespuestasOneHotEncoder(respuestas_seq)

    palabras_indices = vocabulario.obtenerPalabraIndice()
    total_palabras = len(palabras_indices) + 1

    modelo = ChatBot(total_palabras, tam_max_seq, vocabulario.obtenerTokenizer())
    modelo.entrenar(preguntas_seq, y, EPOCAS)

    app.run(host='0.0.0.0', port=5000)
