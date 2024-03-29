from App.Util.FuncionesActivacion import *
import numpy as np

class LSTM:
    TIEMPO_INICIAL = -1
    COMPONENTE_PUERTA_ENTRADA = 1 # También conocido como puerta actualizar
    COMPONENTE_PUERTA_OLVIDO = 2
    COMPONENTE_CANDIDATO = 3
    COMPONENTE_PUERTA_SALIDA = 4

    # ----------------------------------------
    #   Estructura datos de entrada y salida
    # ----------------------------------------
    #
    # tam_entrada: (num_entradas, tam_entrada)
    # tam_salida: (num_entradas, tam_entrada)
    #
    # ----------------------------------------
    #              Capas ocultas
    # ----------------------------------------
    #
    # tam_capa_oculta: las capas internas de la red neuronal
    #
    # ----------------------------------------
    #                  Epocas
    # ----------------------------------------
    #
    # epocas: Pasos en el tiempo
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
    def __init__(self, tam_entrada=(1, 1), tam_salida=(1, 1), tam_oculto=1, epocas=100, rango_aprendizaje=0.5):
        self.componentes = [
            self.COMPONENTE_PUERTA_ENTRADA,
            self.COMPONENTE_PUERTA_OLVIDO,
            self.COMPONENTE_CANDIDATO,
            self.COMPONENTE_PUERTA_SALIDA
        ]
        self.t = 0 # El contador de los pasos en el tiempo
        self.epocas = epocas
        self.rango_aprendizaje = rango_aprendizaje

        self.w = self.inicializacionXavierGlorot(tam_entrada[1], tam_entrada[0]) # Pesos
        self.b = self.inicializacionXavierGlorot(tam_entrada[1], 1) # Sesgos

        self.h = { self.TIEMPO_INICIAL: self.inicializacionXavierGlorot(tam_entrada[0], tam_entrada[1]) } # Estado oculto
        self.c = { self.TIEMPO_INICIAL: self.inicializacionXavierGlorot(tam_entrada[0], tam_entrada[1]) } # Celda

        self.Ws = {} # Pesos de entrada
        self.Rs = {} # Pesos recurrentes
        self.bs = {} # sesgos

        for componente in self.componentes: # Inicialización con la tecnica de Xavier Normalized
            self.inicializaPesosEntrada(componente, (tam_oculto, tam_entrada[0]))
            self.inicializarPesosRecurrentes(componente, (tam_oculto, tam_entrada[0]))
            self.inicializarSesgos(componente, (tam_oculto, 1))
    
    # -------------------------------
    #         Inicialización
    # -------------------------------
    #
    # Esta tecnica se utiliza para abordar el
    # problema de la convergencia lenta o inistable
    # que puede llegar a ocurrir al entrenar redes neuronales.
    #
    def inicializacionXavierGlorot(self, tamEntrada = 1, tamSalida = 1, incluirPasosEnElTiempo = False):
        varianza = np.sqrt(2.0 / (tamEntrada + tamSalida))
        if(incluirPasosEnElTiempo):
            return np.random.normal(0, varianza, size=(self.epocas, tamEntrada, tamSalida))
        else:
            return np.random.normal(0, varianza, size=(tamEntrada, tamSalida))
        
    def inicializaPesosEntrada(self, componente=None, tam=(1,1)):
        self.Ws[componente] = self.inicializacionXavierGlorot(tam[0], tam[1])

    def inicializarPesosRecurrentes(self, componente=None, tam=(1,1)):
        self.Rs[componente] = self.inicializacionXavierGlorot(tam[0], tam[1])

    def inicializarSesgos(self, componente=None, tam=(1,1)):
        self.bs[componente] = self.inicializacionXavierGlorot(tam[0], tam[1])

    def ejecutarPuertaEntrada(self, X: np.ndarray):
        return logistic(
            self.Ws[self.COMPONENTE_PUERTA_ENTRADA] @ X +
            self.Rs[self.COMPONENTE_PUERTA_ENTRADA] @ self.h[self.t - 1] +
            self.bs[self.COMPONENTE_PUERTA_ENTRADA]
        )

    def ejecutarPuertaOlvido(self, X: np.ndarray):
        if(self.t > 0): return
        
        print(X @ self.Ws[self.COMPONENTE_PUERTA_OLVIDO].T)
        print(self.Rs[self.COMPONENTE_PUERTA_OLVIDO])
        print(self.h[self.t - 1])
            
        return logistic(
            self.Ws[self.COMPONENTE_PUERTA_OLVIDO] @ X +
            self.Rs[self.COMPONENTE_PUERTA_OLVIDO] @ self.h[self.t - 1] +
            self.bs[self.COMPONENTE_PUERTA_OLVIDO]
        )

    def ejecutarCandidato(self, X: np.ndarray):
        return tanh(
            self.Ws[self.COMPONENTE_CANDIDATO] @ X +
            self.Rs[self.COMPONENTE_CANDIDATO] @ self.h[self.t - 1] +
            self.bs[self.COMPONENTE_CANDIDATO]
        )

    def ejecutarPuertaSalida(self, X: np.ndarray):
        return logistic(
            self.Ws[self.COMPONENTE_PUERTA_SALIDA] @ X +
            self.Rs[self.COMPONENTE_PUERTA_SALIDA] @ self.h[self.t - 1] +
            self.bs[self.COMPONENTE_PUERTA_SALIDA]
        )
        
    def celdaAdelante(self, X: np.ndarray):
        f_t = self.ejecutarPuertaOlvido(X) # Valor de la puerta de olvido en el paso t
        # print(f_t)
        # i_t = self.ejecutarPuertaEntrada(X) # Valor de la puerta de entrada/actualizacion en el paso t
        # g_t = self.ejecutarCandidato(X) # Valor de la puerta candidata en el paso t
        # o_t = self.ejecutarPuertaSalida(X) # Valor de la puerta de salida en el paso t
        # c_t = self.c[self.t - 1] * f_t + i_t * g_t # Valor de celda en el paso t
        # a_t = c_t * tanh(o_t) # Valor de estado oculto en el paso t
        # y_t = softmax(self.w @ a_t + self.b) # Valor predicción
        
        # cache = (a_t, c_t, self.h[self.t - 1], self.c[self.t - 1], f_t, i_t, g_t, o_t, X)
        # return a_t, c_t, y_t, cache

    def fit(self, X: np.ndarray, y: np.ndarray):
        tiempo = X.shape[0]

        for _ in range(self.epocas):
            for t in range(tiempo):
                self.t = t
                x_t = X[self.t,:].reshape(1, -1)
                self.celdaAdelante(x_t)