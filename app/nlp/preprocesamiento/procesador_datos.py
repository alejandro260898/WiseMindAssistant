import numpy as np
from app.nlp.preprocesamiento.vocabulario import Vocabulario

def generarSecuencias(tokens = [], n = 1, vocabulario = Vocabulario()) -> dict:
    t = 0
    secuenciasEntrada = {}
    secuenciasSalida = {}
    
    for t in range(len(tokens) - n):
        tokens_secuencia = tokens[t:t+n]
        secuenciasEntrada[t] = vocabulario.dameEncoder(tokens_secuencia[0])
        
        for i in range(1, len(tokens_secuencia)):
            secuenciasEntrada[t] = np.vstack(
                (secuenciasEntrada[t], vocabulario.dameEncoder(tokens_secuencia[i]))
            )
        secuenciasEntrada[t] = np.vstack(
            (secuenciasEntrada[t], vocabulario.dameEncoder(vocabulario.dameTokenEND()))
        )
        secuenciasSalida[t] = vocabulario.dameEncoder(tokens[t+n])
        
    return secuenciasEntrada, secuenciasSalida