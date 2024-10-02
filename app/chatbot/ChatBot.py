from keras.api.models import Sequential, load_model
from keras.api.layers import LSTM, Dense, Embedding

from keras_preprocessing.sequence import pad_sequences
from keras_preprocessing.text import Tokenizer
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

class ChatBot:
    TAM_MAX_EMBEDDING = 64
    NUM_NEURONAS = 250
    NOM_ARCHIVO = 'C:/Users/raufa/OneDrive/Escritorio/ImportantThings/clonaciones/ModularProject/App/chatbot/memoria/modelo.h5'

    def __init__(self, total_palabras:int = 1, tam_max_secuencia:int = 1, tokenizer:Tokenizer = None):
        self.tokenizer = tokenizer
        self.tam_max_secuencia = tam_max_secuencia
        
        self.model = Sequential()
        self.model.add(
            Embedding(
                input_dim=total_palabras, 
                output_dim=self.TAM_MAX_EMBEDDING, 
                input_length=tam_max_secuencia
            )
        )
        self.model.add(
            LSTM(self.NUM_NEURONAS, return_sequences=True)
        )
        self.model.add(
            Dense(total_palabras, activation='softmax')
        )
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        
    def entrenar(self, X:np.ndarray = [], y:np.ndarray = [], epocas:int = 100):
        ruta_archivo = Path(self.NOM_ARCHIVO)
        
        if(ruta_archivo.is_file()):
            self.model = load_model(self.NOM_ARCHIVO)
        else :
            historial = self.model.fit(X, y, epochs=epocas, batch_size=16)
            self.model.save(self.NOM_ARCHIVO)
            
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
                
    def predeccir(self, pregunta:str = ''):
        # Ejemplo de predicción
        pregunta_seq = self.tokenizer.texts_to_sequences([pregunta])
        pregunta_seq = pad_sequences(pregunta_seq, maxlen=self.tam_max_secuencia, padding='post')
        # Predecir la respuesta
        prediccion = self.model.predict(pregunta_seq)
        prediccion = prediccion[0] 
        # print(prediccion)
        indices_predicciones = np.argmax(prediccion, axis=-1)
        # print(indices_predicciones)
        # Unimos las palabras separadas por espacio, donde si el indice es 0 se descarta
        respuesta = ' '.join([self.tokenizer.index_word.get(i, '') for i in indices_predicciones if i != 0])
        return respuesta