import re
import numpy as np
from app.nlp.preprocesamiento.tokens import generarTokens
from app.nlp.preprocesamiento.procesador_datos import generarSecuencias, SecuenciaPrediccion
from app.nlp.preprocesamiento.vocabulario import Vocabulario
from app.nlp.preprocesamiento.encoder.oneHotEncoded import OneHotEncoded
from app.nlp.modelo.LSTM import LSTM

RUTA = 'data.txt'
EXP_REGULAR_TOKENS = r'[^a-zA-Záéíóúñ¿?.,\(\)0-9\"\']'
NUM_EPOCAS = 50
FACTORA_APRENDIZAJE = 0.001
PALABRAS_ENTRADA = 10
PALABRAS_PREDICCION = 1
CELDAS_MEMORIA = 100

tokens = generarTokens(RUTA, EXP_REGULAR_TOKENS)
oneHotEncoded = OneHotEncoded()
vocabulario = Vocabulario(tokens, oneHotEncoded)
X, y = generarSecuencias(vocabulario.dameTokens(), PALABRAS_ENTRADA, vocabulario)
_, m = X[0].shape

lstm = LSTM(
    (PALABRAS_ENTRADA, m),
    (PALABRAS_PREDICCION, m),
    (CELDAS_MEMORIA, m),
    NUM_EPOCAS
)
lstm.fit(X, y, FACTORA_APRENDIZAJE)

entrada_usuario = "dark souls"
tokens_usuario = generarTokens(entrada_usuario, EXP_REGULAR_TOKENS, False)
generadorSecuencias = SecuenciaPrediccion(tokens_usuario, vocabulario)
preds = lstm.prediccion(X, generadorSecuencias, vocabulario)
print(preds)