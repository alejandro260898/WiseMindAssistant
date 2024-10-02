
from App.chatbot.ChatBot import ChatBot
from App.chatbot.Vocabulario import Vocabulario

NOM_DATASET = './app/chatbot/data/dataset.xlsx'
COL_PREGUNTA = 'USUARIO'
COL_RESPUESTA = 'ASISTENTE'
EPOCAS = 400

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
palabras = modelo.predeccir('¿como te llamas?')
respuesta = vocabulario.filtrarRespuesta(palabras=palabras)
print(respuesta)
