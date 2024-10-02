from App.nlp.preprocesamiento.tokens import generarTokens
from App.nlp.preprocesamiento.procesador_datos import generarSecuencias, SecuenciaPrediccion
from App.nlp.preprocesamiento.vocabulario import Vocabulario
from App.nlp.preprocesamiento.encoder.oneHotEncoded import OneHotEncoded
from App.nlp.modelo.LSTM import LSTM

RUTA = 'data.txt'
EXP_REGULAR_TOKENS = r'[^a-zA-Záéíóúñ0-9]'
NUM_EPOCAS = 50 #50
FACTORA_APRENDIZAJE = 0.05 #0.001
PALABRAS_ENTRADA = 1
PALABRAS_PREDICCION = 1
CELDAS_MEMORIA = 30 #100

tokens = generarTokens(RUTA, EXP_REGULAR_TOKENS)
oneHotEncoded = OneHotEncoded()
vocabulario = Vocabulario(tokens, oneHotEncoded)
X, y = generarSecuencias(vocabulario.dameTokens(), PALABRAS_ENTRADA, vocabulario)

# print(X[0].shape)
# print(y[0].shape)

_, m = X[0].shape

lstm = LSTM(
    (PALABRAS_ENTRADA, m),
    (PALABRAS_PREDICCION, m),
    (CELDAS_MEMORIA, m),
    NUM_EPOCAS
)
lstm.fit(X, y, FACTORA_APRENDIZAJE)

entrada_usuario = "¿Qué es dark souls?"
tokens_usuario = generarTokens(entrada_usuario, EXP_REGULAR_TOKENS, False)
generadorSecuencias = SecuenciaPrediccion(tokens_usuario, vocabulario)
preds = lstm.prediccion(X, generadorSecuencias, vocabulario)
print(preds)