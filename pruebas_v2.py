import numpy as np
# from app.util.FuncionesActivacion import *

# x_t = np.asanyarray([
#     [0, 0, 1],
#     [0, 1, 0],
#     [1, 0, 0]
# ])
# n_x, m = x_t.shape
# n_a = 1

# a_prev = np.zeros((n_a, m))
# c_prev = np.zeros((n_a, m))
# w_f = np.zeros((n_a, n_x + n_a))
# b_f = np.zeros((n_a, 1))

# print(f"n_x: {x_t.shape[0]}, m: {x_t.shape[1]}")
# print(f"n_a: {a_prev.shape[0]}, m: {a_prev.shape[1]}")
# print(x_t)
# print(a_prev)
# print(w_f)
# print(b_f)
# print('----------------------')

# concat = np.concatenate((a_prev, x_t), axis=0)
# print(concat)
# ft = softmax(w_f @ concat + b_f)
# print(ft)

# x = np.array([[1, 0, 1, 1],
#               [1, 1, 0, 1]])
# wy = np.array([[1, 1],
#                [2, 2]])
# by = np.array([[1]])
# y = wy @ x + by

# a = np.asanyarray([
#     [1, 1, 1, 1],
#     [1, 1, 1, 1]
# ])
# b = np.zeros((5, 4))
# c = np.vstack((a, b))
# print(c)

# """
#     Tam One Hot Encoder original: 5
    
#     Entrada por el usuario
#     [1 1 1][0 0]
#     [1 1 1][0 0]
#     [1 1 1][0 0]    
# """

# x = np.asanyarray([
#     [1, 1, 1],
#     [1, 1, 1],
#     [1, 1, 1],
# ])
# padding = np.zeros((3, 2))
# print(x)
# print(padding)
# x_new = np.hstack((x, padding))
# print(x_new)
# cols_to_delete = np.arange(-2, 0)
# print(np.delete(x, cols_to_delete, axis=1))



# from app.nlp.preprocesamiento.tokens import generarTokens
# from app.nlp.preprocesamiento.procesador_datos import generarSecuencias, SecuenciaPrediccion
# from app.nlp.preprocesamiento.vocabulario import Vocabulario
# from app.nlp.preprocesamiento.encoder.oneHotEncoded import OneHotEncoded

# EXP_REGULAR_TOKENS = r'[^a-zA-Záéíóúñ¿?.,\(\)0-9\"\']'
# RUTA = 'data.txt'

# tokens = generarTokens(RUTA, EXP_REGULAR_TOKENS)
# oneHotEncoded = OneHotEncoded()
# vocabulario = Vocabulario(tokens, oneHotEncoded)
# tokens_original = vocabulario.dameTokens()
# X, y = generarSecuencias(tokens_original, 10, vocabulario)

# print(tokens)
# print(vocabulario.dameToken(40))
# print(vocabulario.dameEncoder('<UNK>'))

# tokens_prediccion = generarTokens("¿Qué es dark souls?", EXP_REGULAR_TOKENS, False)
# print(tokens_prediccion)
# print('---------------------------')
# secuenciaPrediccion = SecuenciaPrediccion(tokens_prediccion, vocabulario)
# x = secuenciaPrediccion.generarSecuencia(10, None)




import nltk
from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical

nltk.download('punkt')

with open("data.txt", "r", encoding="utf-8") as archivo:
    text = archivo.read()

text = 'dark souls es un videojuego'
tokens = nltk.word_tokenize(text.lower())
# print(tokens)

input_sequences = []
output_sequences = []
for i in range(len(tokens)-1):
    input_sequences.append(tokens[i])
    output_sequences.append(tokens[i+1])

# Tokenizar las secuencias
# input_sequences = np.array([nltk.word_tokenize(seq) for seq in input_sequences], dtype=str)
# output_sequences = np.array([nltk.word_tokenize(seq) for seq in output_sequences], dtype=str)
# print(input_sequences)

input_sequences = np.array([1, 2, 3, 4])
output_sequences = np.array([2, 3, 4, 5])
output_sequences = to_categorical(output_sequences, num_classes=6)

# Definir la arquitectura del modelo
model = Sequential()
model.add(Embedding(input_dim=6, output_dim=100, input_length=1))  # input_dim=6 incluye 0
model.add(LSTM(256))
model.add(Dense(6, activation='softmax'))  # Asegúrate de que el output tenga 6 clases

# Compilar el modelo
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
model.fit(input_sequences, output_sequences, epochs=100)

# Generar una respuesta a la entrada del usuario
def generar_respuesta(entrada_usuario:str):
    # Tokenizar la entrada del usuario
    secuencia_entrada_usuario = nltk.word_tokenize(entrada_usuario.lower())
    
    # Predecir el siguiente token en la secuencia
    secuencia_entrada_usuario = np.array([1, 2])
    secuencia_entrada_usuario = pad_sequences(secuencia_entrada_usuario, maxlen=1)
    prediccion = model.predict(secuencia_entrada_usuario)
    
    # Obtener el índice del token predicho
    indice = np.argmax(prediccion)
    
    # Convertir el índice en un token y devolverlo
    return tokens[indice]
    
# generar_respuesta("Que es dark souls")
