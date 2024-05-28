import re
import numpy as np
from tqdm import tqdm
from App.Util.Encoder import OneHotEncoder
from App.Util.ProcesadorDatos import train_test_split
from App.Controller.LSTM import LSTM

EXP_REGULAR_TOKENS = r'[^a-zA-Záéíóúñ¿?.,]'
NUM_EPOCAS = 4000
FACTORA_APRENDIZAJE = 0.080
PALABRAS_ENTRADA = 1
PALABRAS_PREDICCION = 1
CELDAS_MEMORIA = 30

documento = """
    Los manzanos se cultivan en todo el mundo y son las especies más utilizadas del género Malus.
    El árbol se originó en Asia Central, donde su ancestro salvaje, Malus sieversii, todavía se encuentra hoy en día.
    Las manzanas se han cultivado durante miles de años en Asia y Europa y fueron llevadas a América por colonos europeos.
    Las manzanas tienen un significado religioso y mitológico en muchas culturas, incluyendo la tradición nórdica, griega y cristiana europea.
"""

# -- Tokenizar Texto -- #
# Se trata de eliminar todo aquello que no necesites para procesar el texto.
tokens = (re.sub(EXP_REGULAR_TOKENS, ' ', documento.strip())).split(' ')

# Se elimina todas las palabras en blanco
tokens = [token for token in tokens if token != '']
indice_a_palabra = {i: token for i, token in enumerate(tokens)}
oneHotEncoded = OneHotEncoder(tokens)

# Recordar que nuestra salida debe ser la palabra siguiente de cada palabra
X = oneHotEncoded[:-1]
y = oneHotEncoded[1:]
_, m = X.shape

x_train, y_train, x_test, y_test = train_test_split(X, y)

lstm = LSTM(
    (PALABRAS_ENTRADA, m),
    (PALABRAS_PREDICCION, m),
    (CELDAS_MEMORIA, m),
    NUM_EPOCAS
) 
lstm.fit(x_train, y_train, FACTORA_APRENDIZAJE)

preds = lstm.prediccion(x_test)
indices = np.argmax(preds, axis=0)
print(indices)