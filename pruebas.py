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



from app.nlp.preprocesamiento.tokens import generarTokens
from app.nlp.preprocesamiento.procesador_datos import generarSecuencias
from app.nlp.preprocesamiento.vocabulario import Vocabulario
from app.nlp.preprocesamiento.encoder.oneHotEncoded import OneHotEncoded

EXP_REGULAR_TOKENS = r'[^a-zA-Záéíóúñ¿?.,\(\)0-9\"\']'
RUTA = 'data.txt'

tokens = generarTokens(RUTA, EXP_REGULAR_TOKENS)
oneHotEncoded = OneHotEncoded()
vocabulario = Vocabulario(tokens, oneHotEncoded)
X, y = generarSecuencias(tokens, 10, vocabulario)

# print(tokens)
# print(vocabulario.dameToken(40))
# print(vocabulario.dameEncoder('dark'))
