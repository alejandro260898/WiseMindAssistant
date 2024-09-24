import numpy as np
from app.nlp.preprocesamiento.vocabulario import Vocabulario

def generarSecuencias(tokens:list = [], n = 1, vocabulario:Vocabulario = None) -> dict:
    n = n - 1
    t = 0
    secuenciasEntrada = {}
    secuenciasSalida = {}
    
    for t in range(len(tokens) - n):
        tokens_secuencia = tokens[t:t+n]
        tokens_secuencia.append(vocabulario.dameTokenEND())
        
        if(len(tokens_secuencia) < n):
            for _ in range(len(tokens_secuencia), n):
                tokens_secuencia.append(vocabulario.dameTokenPAD())
        # else no agregar el padding
        
        secuenciasEntrada[t] = vocabulario.dameEncoder(tokens_secuencia[0])
        for i in range(1, len(tokens_secuencia)):
            secuenciasEntrada[t] = np.vstack(
                (secuenciasEntrada[t], vocabulario.dameEncoder(tokens_secuencia[i]))
            )
        secuenciasSalida[t] = vocabulario.dameEncoder(tokens[t+n])
        
    return secuenciasEntrada, secuenciasSalida

class SecuenciaPrediccion:
    vocabulario = None
    tokens = []
    t = 0
    
    def __init__(self, tokens:list = [], vocabulario:Vocabulario = None):
        self.tokens = tokens
        self.vocabulario = vocabulario
        
    def generarSecuencia(self, n = 1, prediccion = None):
        if(prediccion): self.tokens.append(prediccion)
        tokens_secuencia = self.tokens[self.t:self.t+n]
        # print(tokens_secuencia)
        # print('\n')
        
        if(len(tokens_secuencia) < n):
            for _ in range(len(tokens_secuencia), n):
                tokens_secuencia.append(self.vocabulario.dameTokenPAD())
        else:
            self.t += 1
        
        secuencia_entrada = self.vocabulario.dameEncoder(tokens_secuencia[0])
        for i in range(1, len(tokens_secuencia)):
            secuencia_entrada = np.vstack(
                (secuencia_entrada, self.vocabulario.dameEncoder(tokens_secuencia[i]))
            )
        return secuencia_entrada
    
    def dameTiempo(self):
        return self.t
        