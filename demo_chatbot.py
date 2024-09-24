"""
# Elección de Datos

Para un chat bot es recomendable elegir todas las preguntas como entrada (X) y 
las respuestas como la predicción esperada (y).

"""
PREGUNTA = "p"
RESPUESTA = "r"

pregunta = "Buenos días"
data = [
    {PREGUNTA: "¿Quién es el primer poseedor del Lord Soul en Dark Souls?", RESPUESTA: "El primer poseedor del Lord Soul es Gwyn, el Señor de la Luz Solar"},
    {PREGUNTA: "¿Cuál es la relación entre Seath el Descamado y los dragones?", RESPUESTA: "Seath es un dragón albino sin escamas, lo que lo hace vulnerable"},
    {PREGUNTA: "Hola buenos días", RESPUESTA: "Cómo estas NOMUSUARIO"},
]
preguntas =  [item[PREGUNTA] for item in data]
respuestas = [item[RESPUESTA] for item in data]
vocabulario = preguntas + respuestas

"""
# Pre-Procesamiento

Los modelos de aprerndizaje profundo no pueden entender cadenas, 
así que debemos transformar a una forma númerica. El objeto 'Tokenizer' nos ayuda con esta tarea.

"""

from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.api.utils import to_categorical
from pathlib import Path
import pickle

NOM_ARCHIVO_TOKENIZER = 'vocabulario.pkl'

ruta_archivo = Path(NOM_ARCHIVO_TOKENIZER)

if(ruta_archivo.is_file()):
    with open(NOM_ARCHIVO_TOKENIZER, 'rb') as file:
        tokenizer = pickle.load(file)
else:
    tokenizer = Tokenizer(filters='¿?_<>.', oov_token='<UNK>')
    # 'fit_on_texts': Entrena con tu vocabulario donde a cada palabra (token) se le asigna un indice entero, en donde el token que más se repite tiene el indice menor.
    tokenizer.fit_on_texts(vocabulario)
    with open(NOM_ARCHIVO_TOKENIZER, 'wb') as file:
        pickle.dump(tokenizer, file)
        
# 'texts_to_sequences': Convierte en secuencias donde si una cadena tiene 5 palabras será un array de 5 indice los cuales representan a las palabras.
preguntas_seq  = tokenizer.texts_to_sequences(preguntas)
respuestas_seq = tokenizer.texts_to_sequences(respuestas)
# print(preguntas_seq)
# print(respuestas_seq)

# Obtener la pregunta y la respuesta con el tamaño mayor
tam_max_pregunta = max(len(seq) for seq in preguntas_seq)
tam_max_respuesta = max(len(seq) for seq in respuestas_seq)
# Obtener la secuencia con el mayor tamaño
tam_max_secuencia = max(tam_max_pregunta, tam_max_respuesta)
# Adaptamos las respuestas y preguntas para que tengan el mismo tamaño para no tener errores en el entrenamiento.
preguntas_seq  = pad_sequences(preguntas_seq, maxlen=tam_max_secuencia, padding='post') # 'post' es para agregar el padding al final.
respuestas_seq = pad_sequences(respuestas_seq, maxlen=tam_max_secuencia, padding='post')
# print(preguntas_seq)
# print(respuestas_seq)

# Convertimos las respuestas a su representación One Hot Encoder.
# 'tokenizer.word_index': devuelve un diccionario token => indice del vocabulario
palabras_indices = tokenizer.word_index
total_palabras = len(palabras_indices) + 1 # El +1 es por el padding ya que también cuenta como token.
y = to_categorical(respuestas_seq, num_classes=total_palabras) 
# print(tokenizer.word_index)
# print(y)

from keras.api.models import Sequential, load_model
from keras.api.layers import LSTM, Dense, Embedding
import numpy as np

"""
# Construir el modelo

El objeto 'Sequential' declara un modelo simple de aprendizaje profundo util para RNN.
El objeto 'Embedding' ayuda a transformar cada vector de indices a un vector de n dimensiones 
especificado en 'output_dim'.
El objeto 'LSTM' define el modelo a utilizar con un tam de n neuronas en su capa oculta.
"""
TAM_MAX_EMBEDDING = 64
NUM_NEURONAS = 256
EPOCAS = 200
NOM_ARCHIVO = 'modelo.h5'

ruta_archivo = Path(NOM_ARCHIVO)

if(ruta_archivo.is_file()):
    model = load_model(NOM_ARCHIVO)
else :
    model = Sequential()
    model.add(
        Embedding(
            input_dim=total_palabras, 
            output_dim=TAM_MAX_EMBEDDING, 
            input_length=tam_max_secuencia
        )
    )
    model.add(
        LSTM(NUM_NEURONAS, return_sequences=True)
    )
    model.add(
        Dense(total_palabras, activation='softmax')
    )
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    
    historial = model.fit(preguntas_seq, y, epochs=EPOCAS, batch_size=16)
    model.save(NOM_ARCHIVO)

    import matplotlib.pyplot as plt

    # Graficar la pérdida (loss)
    plt.plot(historial.history['loss'], label='Pérdida de entrenamiento')
    # plt.plot(historial.history['val_loss'], label='Pérdida de validación')
    plt.title('Evolución de la pérdida durante el entrenamiento')
    plt.xlabel('Épocas')
    plt.ylabel('Pérdida')
    plt.legend()
    plt.show()

    # Graficar la precisión (si es aplicable)
    if 'accuracy' in historial.history:
        plt.plot(historial.history['accuracy'], label='Precisión de entrenamiento')
        # plt.plot(historial.history['val_accuracy'], label='Precisión de validación')
        plt.title('Evolución de la precisión durante el entrenamiento')
        plt.xlabel('Épocas')
        plt.ylabel('Precisión')
        plt.legend()
        plt.show()




# Ejemplo de predicción
pregunta_seq = tokenizer.texts_to_sequences([pregunta])
pregunta_seq = pad_sequences(pregunta_seq, maxlen=tam_max_secuencia, padding='post')
# Predecir la respuesta
prediccion = model.predict(pregunta_seq)
prediccion = prediccion[0] 
# print(prediccion)
indices_predicciones = np.argmax(prediccion, axis=-1)
# print(indices_predicciones)
# Unimos las palabras separadas por espacio, donde si el indice es 0 se descarta
respuesta = ' '.join([tokenizer.index_word.get(i, '') for i in indices_predicciones if i != 0])
print(respuesta)

