from app.nlp.modelo.funciones_activacion.funciones_activacion import *
from app.nlp.preprocesamiento.procesador_datos import SecuenciaPrediccion
from app.nlp.preprocesamiento.vocabulario import Vocabulario
import matplotlib.pyplot as plt
import numpy as np

class LSTM:
    TIEMPO_INICIAL = -1

    # ----------------------------------------
    #   Estructura datos de entrada y salida
    # ----------------------------------------
    #
    # tam_entrada: (num_entradas, tam_entrada)
    # tam_salida: (num_entradas, tam_entrada)
    #
    # ----------------------------------------
    #                  Epocas
    # ----------------------------------------
    #
    # epocas: Pasos en el tiempo que será retroalimentado el modelo
    #
    # ----------------------------------------
    #                   Cache
    # ----------------------------------------
    # 
    # En la cache iremos guardando los estados 
    # ocultos, los estados de celda y las salidas.
    # Esta información no va a servir para el 
    # backpropagation. (a, c, y)
    #
    def __init__(self, tam_entrada=(1, 1), tam_salida=(1, 1), tam_oculto=(1, 1), epocas=100):
        self.cache = []
        self.T = self.TIEMPO_INICIAL # Contador de los pasos en el tiempo
        self.epocas = epocas
        
        self.tam_entrada  = tam_entrada
        self.tam_salida  = tam_salida
        
        n_x, m = tam_entrada
        n_a, _ = tam_oculto
        n_y, _ = tam_salida

        # Puerta Entrada / Actualizar
        self.Wi = self.inicializacionXavierGlorot((n_a, n_a + n_x))
        self.bi = np.zeros((n_a, 1))
        # Puerta Olvido
        self.Wf = self.inicializacionXavierGlorot((n_a, n_a + n_x))
        self.bf = np.zeros((n_a, 1))
        # Puerta Candidato
        self.Wc = self.inicializacionXavierGlorot((n_a, n_a + n_x))
        self.bc = np.zeros((n_a, 1))
        # Puerta Salida
        self.Wo = self.inicializacionXavierGlorot((n_a, n_a + n_x))
        self.bo = np.zeros((n_a, 1))
        # Predicción
        self.Wy = self.inicializacionXavierGlorot((n_y, n_a))
        self.by = np.zeros((n_y, 1))
        # Estado Oculto
        self.h = { self.T: np.zeros((n_a, m)) }
        # Estado Celda
        self.c = { self.T: np.zeros((n_a, m)) }
        
    # -------------------------------
    #         Inicialización
    # -------------------------------
    #
    # Esta tecnica se utiliza para abordar el
    # problema de la convergencia lenta o inistable
    # que puede llegar a ocurrir al entrenar redes neuronales.
    #
    def inicializacionXavierGlorot(self, dimension=(1, 1)):
        varianza = np.sqrt(2.0 / (dimension[0] + dimension[1]))
        return np.random.normal(0, varianza, size=dimension)

    def ejecutarPuertaEntrada(self, x_t: np.ndarray):
        concat = np.concatenate((x_t, self.h[self.T - 1]), axis=0)
        return logistic_hidden(self.Wi @ concat + self.bi)

    def ejecutarPuertaOlvido(self, x_t: np.ndarray):
        concat = np.concatenate((x_t, self.h[self.T - 1]), axis=0)
        return logistic_hidden(self.Wf @ concat + self.bf)

    def ejecutarCandidato(self, x_t: np.ndarray):
        concat = np.concatenate((x_t, self.h[self.T - 1]), axis=0)
        return tanh(self.Wc @ concat + self.bc)

    def ejecutarPuertaSalida(self, x_t: np.ndarray):
        concat = np.concatenate((x_t, self.h[self.T - 1]), axis=0)
        return logistic_hidden(self.Wo @ concat + self.bo)
        
    def celdaAdelante(self, x_t: np.ndarray):
        f_t = self.ejecutarPuertaOlvido(x_t)        # Valor de la puerta de olvido en el paso t
        i_t = self.ejecutarPuertaEntrada(x_t)       # Valor de la puerta de entrada/actualizacion en el paso t
        cc_t = self.ejecutarCandidato(x_t)          # Valor de la puerta candidata en el paso t
        o_t = self.ejecutarPuertaSalida(x_t)        # Valor de la puerta de salida en el paso t
        c_t = self.c[self.T - 1] * f_t + i_t * cc_t # Valor de celda en el paso t
        h_t = c_t * tanh(o_t)                       # Valor de estado oculto en el paso t
        y_pred = softmax(self.Wy @ h_t + self.by)   # Valor predicción
        
        self.h[self.T] = h_t
        self.c[self.T] = c_t
        
        self.cache.append((h_t, c_t, self.h[self.T - 1], self.c[self.T - 1], f_t, i_t, cc_t, o_t, x_t))
        return y_pred
    
    def celdaAtras(self, dy: np.ndarray, dh_next: np.ndarray, dc_next: np.ndarray):
        h_next, c_next, h_prev, c_prev, f_t, i_t, cc_t, o_t, x_t = self.cache.pop()
        
        do = dh_next * tanh(c_next) * o_t * (1 - o_t)
        dcc = (dc_next * i_t + o_t * (1 - tanh(cc_t)**2) * i_t * dh_next) * (1 - cc_t**2)
        di = (dc_next * cc_t + o_t * (1 - tanh(cc_t)**2) * cc_t * dh_next) * i_t * (1 - i_t)
        df = (dc_next * c_prev + o_t * (1 - tanh(cc_t)**2) * c_prev * dh_next) * f_t * (1 - f_t)
        
        dWo = np.dot(do, np.concatenate((h_prev, x_t)).T)
        dbo = np.sum(do, axis=1, keepdims=True)
        
        dWc = np.dot(dcc, np.concatenate((h_prev, x_t)).T)
        dbc = np.sum(dcc, axis=1, keepdims=True)
        
        dWi = np.dot(di, np.concatenate((h_prev, x_t)).T)
        dbi = np.sum(di, axis=1, keepdims=True)
        
        dWf = np.dot(df, np.concatenate((h_prev, x_t)).T)
        dbf = np.sum(df, axis=1, keepdims=True)
        
        dWy = np.dot(dy, h_next.T)
        dby = np.sum(dy, axis=1, keepdims=True)
        
        d_concat = (np.dot(self.Wf.T, df) + np.dot(self.Wi.T, di) + np.dot(self.Wc.T, dcc) + np.dot(self.Wo.T, do))
        dh_prev = d_concat[:self.h[self.T].shape[0], :]
        dx = d_concat[self.h[self.T].shape[0]:, :]
        
        return dWf, dbf, dWi, dbi, dWc, dbc, dWo, dbo, dWy, dby, dh_prev, dx

    def fit(self, X, y, factor_aprendizaje = 0.001):
        secuencias = len(X)
        print(f"Secuencias por epoca: {secuencias}")
        print(f"Total de epocas: {self.epocas}")
        
        perdidas = []
        self.T = 0
        
        for epoca in range(self.epocas): # Retroalimentación
            total_loss = 0
            
            for t in range(0, secuencias):
                x_t = X[t]
                y_t = y[t]
                
                y_pred = self.celdaAdelante(x_t)
                
                loss = -np.sum(y_t * np.log(y_pred))
                total_loss += loss
                
                dy = y_pred - y_t
                dh_next = np.zeros_like(self.h[self.T])
                dc_next = np.zeros_like(self.c[self.T])
                
                dWf, dbf, dWi, dbi, dWc, dbc, dWo, dbo, dWy, dby, dh_next, dx = self.celdaAtras(dy, dh_next, dc_next)
                
                self.Wf -= factor_aprendizaje * dWf
                self.bf -= factor_aprendizaje * dbf
                self.Wi -= factor_aprendizaje * dWi
                self.bi -= factor_aprendizaje * dbi
                self.Wc -= factor_aprendizaje * dWc
                self.bc -= factor_aprendizaje * dbc
                self.Wo -= factor_aprendizaje * dWo
                self.bo -= factor_aprendizaje * dbo
                self.Wy -= factor_aprendizaje * dWy
                self.by -= factor_aprendizaje * dby
                
                self.T += 1
            
            avg_loss = total_loss / secuencias
            perdidas.append(avg_loss)
            print(f"Epoca {epoca + 1}/{self.epocas}, Pérdida: {avg_loss}")
            
        plt.plot(perdidas)
        plt.xlabel("Época")
        plt.ylabel("Pérdida")
        plt.title("Pérdida durante el Entrenamiento")
        plt.show()
            
    def prediccion(self, X: np.ndarray, generador_secuencias = SecuenciaPrediccion(), vocabulario = Vocabulario()):
        self.h[self.TIEMPO_INICIAL] = np.zeros_like(self.h[self.TIEMPO_INICIAL])
        self.c[self.TIEMPO_INICIAL] = np.zeros_like(self.c[self.TIEMPO_INICIAL])
        n_x, _ = self.tam_entrada
        
        predicciones = []
        prediccion = None

        self.T = 0
        while prediccion != vocabulario.dameTokenEND() and generador_secuencias.dameTiempo() < 10:
            x_t = generador_secuencias.generarSecuencia(n_x, prediccion)

            y_pred = self.celdaAdelante(x_t)       
            indice = np.argmax(y_pred)
            
            prediccion = vocabulario.dameToken(indice)
            predicciones.append(prediccion)
            
            self.T += 1
            
        return predicciones
    
    def guardar():
        return
    
    def cargar():
        return