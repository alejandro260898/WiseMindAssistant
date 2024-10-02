import pickle
import pandas as pd
from pathlib import Path
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.api.utils import to_categorical

class Vocabulario:
    TAM_MAX_SECUENCIA = 0
    TOKEN_OOV = '<UNK>'
    MODO_LECTURA = 'rb'
    MODO_ESCRITURA = 'wb'
    NOM_ARCHIVO_TOKENIZER = 'C:/Users/franc/Documents/GitHub/Proyecto_Modular/WiseMindAssistant/app/chatbot/memoria/vocabulario.pkl'
    
    def __init__(self) -> None:
        pass
    
    def obtenerTokenizer(self):
        return self.tokenizer
    
    def obtenerPreguntas(self):
        return self.preguntas
    
    def obtenerRespuestas(self):
        return self.respuestas
    
    def obtenerRespuestasOneHotEncoder(self, secuencias):
        palabras_indices = self.tokenizer.word_index
        total_palabras = len(palabras_indices) + 1 # El +1 es por el padding ya que también cuenta como token.
        y = to_categorical(secuencias, num_classes=total_palabras) 
        return y
    
    def obtenerPalabraIndice(self):
        return self.tokenizer.word_index
    
    def leerData(self, nom_archivo:str = '', nomColPregunta:str = 'A', nomColRespuesta:str = 'B'):
        if(len(nom_archivo) == 0): return False
        else:
            data = pd.read_excel(nom_archivo)
            
            self.preguntas = []
            for pregunta in data[nomColPregunta]:
                self.preguntas.append(pregunta.lower())
            self.respuestas = []
            for respuesta in data[nomColRespuesta]:
                self.respuestas.append(respuesta.lower())
            
            self.vocabulario = self.preguntas + self.respuestas
            return True
        
    def cargar(self):
        ruta_archivo = Path(self.NOM_ARCHIVO_TOKENIZER)
        
        if(ruta_archivo.is_file()):
            with open(self.NOM_ARCHIVO_TOKENIZER, self.MODO_LECTURA) as file:
                self.tokenizer = pickle.load(file)
            return True
        else:
            self.tokenizer = Tokenizer(filters='"#$%&()*+-/:;<=>@[\\]^`{|}~', oov_token=self.TOKEN_OOV)
            self.entrenarVocabulario(self.vocabulario)
            return False
        
    def entrenarVocabulario(self, vocabulario = []):
        self.tokenizer.fit_on_texts(vocabulario)
        with open(self.NOM_ARCHIVO_TOKENIZER, self.MODO_ESCRITURA) as file:
            pickle.dump(self.tokenizer, file)
    
    def crearSecuencias(self, datos = []):
        return self.tokenizer.texts_to_sequences(datos)
    
    def crearTamMaxSecuencia(self, vocabulario_seq = []):
        self.tam_max_seq = max(len(seq) for seq in vocabulario_seq)
        return self.tam_max_seq
    
    def agregarPadding(self, secuencias = []):
        return pad_sequences(secuencias, maxlen=self.tam_max_seq, padding='post')

    def filtrarRespuesta(self, palabras:list = []):
        if(len(palabras) == 0): return "Lo siento por el momento no tengo una respuesta para esa pregunta."
        else:
            palabraAnt = None
            respuestaCoherente = False
            for palabra in palabras:
                if(palabra == palabraAnt):          
                    respuestaCoherente = False
                    break
                else:
                    respuestaCoherente = True
                    palabraAnt = palabra
                
            if(respuestaCoherente): 
                respuesta = " ".join(palabras)
            else:
                respuesta = "Lo siento por el momento no tengo una respuesta para esa pregunta."
            return respuesta