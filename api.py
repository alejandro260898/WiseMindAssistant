from flask import Flask, jsonify, request
from app.chatbot.Vocabulario import Vocabulario
from app.chatbot.ChatBot import ChatBot

app = Flask(__name__)

NOM_DATASET = './app/chatbot/data/dataset.xlsx'
COL_PREGUNTA = 'USUARIO'
COL_RESPUESTA = 'ASISTENTE'
EPOCAS = 200

modelo = None

@app.route('/')
def inicio():
    return 'Esta funcionando...'

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
    print(tam_max_seq)
    preguntas_seq = vocabulario.agregarPadding(preguntas_seq)
    respuestas_seq = vocabulario.agregarPadding(respuestas_seq)

    y = vocabulario.obtenerRespuestasOneHotEncoder(respuestas_seq)

    palabras_indices = vocabulario.obtenerPalabraIndice()
    total_palabras = len(palabras_indices) + 1

    modelo = ChatBot(total_palabras, tam_max_seq, vocabulario.obtenerTokenizer())
    modelo.entrenar(preguntas_seq, y, EPOCAS)

    app.run(host='0.0.0.0', port=5000)