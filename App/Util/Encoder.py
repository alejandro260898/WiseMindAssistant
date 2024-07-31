import numpy as np

def OneHotEncoder(tokens = []):
    vocabulario = {}
    
    if(len(tokens) == 0): return None, vocabulario
    else:
        tokensUnicos = sorted(list(set(tokens))) # Obtener una lista sin palabras repetidas
        indicesTokens = {categoria: i for i, categoria in enumerate(tokensUnicos)}
        
        oneHotEncoded = np.zeros((len(tokens), len(tokensUnicos)))
        for i, categoria in enumerate(tokens):
            indice = indicesTokens[categoria]
            oneHotEncoded[i, indice] = 1
            vocabulario[categoria] = oneHotEncoded[i]
        return oneHotEncoded, vocabulario