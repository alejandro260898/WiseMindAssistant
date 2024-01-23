import numpy as np

def OneHotEncoder(tokens = []):
    if(len(tokens) == 0):
        return None
    else:
        tokensUnicos = list(set(tokens))
        indicesTokens = {categoria: i for i, categoria in enumerate(tokensUnicos)}

        oneHotEncoded = np.zeros((len(tokens), len(tokensUnicos)))
        for i, categoria in enumerate(tokens):
            indice = indicesTokens[categoria]
            oneHotEncoded[i, indice] = 1
        return oneHotEncoded