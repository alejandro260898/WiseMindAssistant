import re
import numpy as np
from tqdm import tqdm
from app.util.Encoder import OneHotEncoder
from app.util.ProcesadorDatos import train_test_split
from app.controller.LSTM import LSTM

EXP_REGULAR_TOKENS = r'[^a-zA-Záéíóúñ¿?.,\(\)0-9\"\']'
NUM_EPOCAS = 10
FACTORA_APRENDIZAJE = 0.08
PALABRAS_ENTRADA = 10
PALABRAS_PREDICCION = 1
CELDAS_MEMORIA = 50

def generar_secuencias(X: np.ndarray, n: int):
    secuenciasEntrada = {}
    secuenciasSalida = {}
    
    for t in range(len(X) - n):
        secuenciasEntrada[t] = X[t:t+n]
        secuenciasSalida[t] = X[t+n]
    return secuenciasEntrada, secuenciasSalida

def adaptarTexto(data: str):
    # -- Tokenizar Texto -- #
    # Se trata de eliminar todo aquello que no necesites para procesar el texto.
    tokens = re.sub(EXP_REGULAR_TOKENS, ' ', data.lower().strip())
    tokens = re.findall(r'\b\w+\b|[^\w\s]', tokens)
    
    # Se elimina todas las palabras en blanco
    tokens = [token for token in tokens if token != '']
    print(f"Total de palabras: {len(tokens)}")
    
    return tokens



with open('data.txt', 'r', encoding='utf-8') as archivo:
    documento = archivo.read()

# Define el tamaño de la secuencia de entrada
tokens = adaptarTexto(documento)
tokens.insert(0, '<UNK>')
tokens.append('<END>')

indicesPalabras = {i: token for i, token in enumerate(tokens)}
X, vocabulario = OneHotEncoder(tokens)
n, m = X.shape

# Recordar que nuestra salida debe ser la palabra siguiente de cada palabra
X, y = generar_secuencias(X, PALABRAS_ENTRADA)
# x_train, y_train, x_test, y_test = train_test_split(X, y)

lstm = LSTM(
    (PALABRAS_ENTRADA, m),
    (PALABRAS_PREDICCION, m),
    (CELDAS_MEMORIA, m),
    NUM_EPOCAS
)
lstm.fit(X, y, FACTORA_APRENDIZAJE)

tokens = adaptarTexto("¿Que es Dark Souls?")
X = np.empty((0, m))
for token in tokens:
    if(token in vocabulario):
        X = np.vstack((X, vocabulario[token]))
    else:
        X = np.vstack((X, vocabulario['<UNK>']))

preds = lstm.prediccion(X)
for pred in preds:
    indice = np.argmax(pred)
    print(indice)
    print(indicesPalabras[indice])