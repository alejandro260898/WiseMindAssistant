import re
import numpy as np
from tqdm import tqdm
from App.Util.Encoder import OneHotEncoder
from App.Util.ProcesadorDatos import train_test_split
from App.Controller.LSTM import LSTM

EXP_REGULAR_TOKENS = r'[^a-zA-Záéíóúñ.]'
NUM_EPOCAS = 500
TAM_ESTADO_OCULTO = 3
LEARNING_RATE = 0.5

documento = """
    Los manzanos se cultivan en todo el mundo y son las especies más utilizadas del género Malus.
    El árbol se originó en Asia Central, donde su ancestro salvaje, Malus sieversii, todavía se encuentra hoy en día.
    Las manzanas se han cultivado durante miles de años en Asia y Europa y fueron llevadas a América por colonos europeos.
    Las manzanas tienen un significado religioso y mitológico en muchas culturas, incluyendo la tradición nórdica, griega y cristiana europea.
"""
documento = "Hola mundo alegre"

# -- Tokenizar Texto -- #
# Se trata de eliminar todo aquello que no necesites para procesar el texto.
tokens = (re.sub(EXP_REGULAR_TOKENS, ' ', documento.strip())).split(' ')
tokens = [token for token in tokens if token != '']
oneHotEncoded = OneHotEncoder(tokens)

# Recordar que nuestra salida debe ser la palabra siguiente de cada palabra
X = oneHotEncoded[:-1]
y = oneHotEncoded[1:]
# print(oneHotEncoded)

print("Valor de X")
print(X)
print("Valor de Y")
print(y)

x_train, y_train, x_test, y_test = train_test_split(X, y)
# print(x_train)
# print(y_train)

lstm = LSTM(
    X.shape,
    y.shape,
    TAM_ESTADO_OCULTO,
    NUM_EPOCAS,
    LEARNING_RATE
)

lstm.fit(X, y)