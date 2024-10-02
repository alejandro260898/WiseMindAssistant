from flask import Flask, jsonify, request
from App.chatbot.Vocabulario import Vocabulario
from App.chatbot.ChatBot import ChatBot
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
NOM_DATASET = './app/chatbot/data/dataset.xlsx'
COL_PREGUNTA = 'USUARIO'
COL_RESPUESTA = 'ASISTENTE'
EPOCAS = 450

modelo = None

@app.route('/proof')
def proof():
    return jsonify({"message": "hola cdscsdcs"})  



@app.route('/pregunta', methods=['POST'])
def darPregunta():
    pregunta = request.get_json()
    print(pregunta.get('message'))
    return jsonify({ 'respuesta': modelo.predeccir(pregunta.get('message')) })

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
