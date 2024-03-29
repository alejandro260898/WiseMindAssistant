import numpy as np
import sys

# Recuperamos el texto y lo convertimos a mayusculas.
raw_text = open('./los3.txt').read()
raw_text = raw_text.lower()
# print(raw_text)

# Obtenemos todos los caracteres diferentes en una lista ordenada.
chars = sorted(list(set(raw_text)))
# print(chars)

# Crea un dicccionario (clave, valor) para representar cada letra del vocabulario.
chars_to_int = dict((c, i) for i, c in enumerate(chars))
# print(chars_to_int)

# Se muestra la cuenta del total de caractes y los caracteres diferentes.
n_chars = len(raw_text)
n_vocab = len(chars)
# print(n_chars)
# print(n_vocab)

seq_length = 100
dataX = []
dataY = []

for i in range(0, n_chars - seq_length, 1):
    seq_in = raw_text[i:i + seq_length]
    seq_out = raw_text[i + seq_length]
    dataX.append([chars_to_int[char] for char in seq_in])
    dataY.append(chars_to_int[seq_out])
n_patterns = len(dataX)
# print("Total patrones: ", n_patterns)

# remodelar X para que sea [muestras, pasos de tiempo, características]
X = np.reshape(dataX, (n_patterns, seq_length, 1))
# normalizacion
X = X / float(n_vocab)
print(X)
