from App.Util.FuncionesActivacion import *
import numpy as np

class LSTM:
    TIEMPO_INICIAL = -1
    COMPONENTE_PUERTA_ENTRADA = 1
    COMPONENTE_PUERTA_OLVIDO = 2
    COMPONENTE_CANDIDATO = 3
    COMPONENTE_PUERTA_SALIDA = 4

    # ----------------------------------------
    #   Estructura datos de entrada y salida
    # ----------------------------------------
    #
    # input_size: (num_entradas, tam_entrada)
    # output_size: (num_entradas, tam_entrada)
    #
    # ----------------------------------------
    #              Capas ocultas
    # ----------------------------------------
    #
    # hidden_size: tam_capa_oculta
    #
    def __init__(self, tam_entrada=(1, 1), tam_salida=(1, 1), tam_oculto=1, epocas=100, rango_aprendizaje=0.5):
        self.componentes = [
            self.COMPONENTE_PUERTA_ENTRADA,
            self.COMPONENTE_PUERTA_OLVIDO,
            self.COMPONENTE_CANDIDATO,
            self.COMPONENTE_PUERTA_SALIDA
        ]
        self.t = 0
        self.epocas = epocas
        self.rango_aprendizaje = rango_aprendizaje

        self.w = np.zeros((tam_entrada[0], tam_entrada[1]))
        self.b = np.zeros(((tam_entrada[0]), 1))

        self.h = { self.TIEMPO_INICIAL: np.zeros((tam_entrada[0], tam_entrada[1])) }
        self.c = { self.TIEMPO_INICIAL: np.zeros((tam_entrada[0], tam_entrada[1])) }

        self.Ws = {} # Pesos de entrada
        self.Rs = {} # Pesos recurrentes
        self.bs = {} # sesgos

        for componente in self.componentes: # Inicialización Xavier Normalized
            self.inicializaPesosEntrada(componente, (tam_oculto, tam_entrada[0]))
            self.inicializarPesosRecurrentes(componente, (tam_oculto, tam_entrada[0]))
            self.inicializarSesgos(componente, (tam_oculto, 1))

    def inicializaPesosEntrada(self, componente=None, tam=(1,1)):
        self.Ws[componente] = np.ones(tam)

    def inicializarPesosRecurrentes(self, componente=None, tam=(1,1)):
        self.Rs[componente] = np.ones(tam)

    def inicializarSesgos(self, componente=None, tam=(1,1)):
        self.bs[componente] = np.ones(tam)

    def ejecutarPuertaEntrada(self, X):
        return logistic(
            self.Ws[self.COMPONENTE_PUERTA_ENTRADA] @ X +
            self.Rs[self.COMPONENTE_PUERTA_ENTRADA] @ self.h[self.t - 1] +
            self.bs[self.COMPONENTE_PUERTA_ENTRADA]
        )

    def ejecutarPuertaOlvido(self, X):
        return logistic(
            self.Ws[self.COMPONENTE_PUERTA_OLVIDO] @ X +
            self.Rs[self.COMPONENTE_PUERTA_OLVIDO] @ self.h[self.t - 1] +
            self.bs[self.COMPONENTE_PUERTA_OLVIDO]
        )

    def ejecutarCandidato(self, X):
        return tanh(
            self.Ws[self.COMPONENTE_CANDIDATO] @ X +
            self.Rs[self.COMPONENTE_CANDIDATO] @ self.h[self.t - 1] +
            self.bs[self.COMPONENTE_CANDIDATO]
        )

    def ejecutarPuertaSalida(self, X):
        return logistic(
            self.Ws[self.COMPONENTE_PUERTA_SALIDA] @ X +
            self.Rs[self.COMPONENTE_PUERTA_SALIDA] @ self.h[self.t - 1] +
            self.bs[self.COMPONENTE_PUERTA_SALIDA]
        )

    def fit(self, X, y):
        for _ in range(self.epocas):
            f_t = self.ejecutarPuertaOlvido(X)
            i_t = self.ejecutarPuertaEntrada(X)
            g_t = self.ejecutarCandidato(X)
            o_t = self.ejecutarPuertaSalida(X)