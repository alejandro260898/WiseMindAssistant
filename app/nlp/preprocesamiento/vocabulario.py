import numpy as np
from app.nlp.preprocesamiento.encoder.oneHotEncoded import OneHotEncoded 

class Vocabulario:
    TOKE_END = "<END>"
    TOKE_PAD = "<PAD>"
    TOKE_UNK = "<UNK>"
    lista_indice_token = {}
    lista_token_encoder = {}
    tokens_originales = [] 
    
    def __init__(self, tokens:list = [], encoder = OneHotEncoded()):
        self.tokens_originales = tokens.copy()
        tokens.append(self.TOKE_END)
        tokens.append(self.TOKE_PAD)
        tokens.append(self.TOKE_UNK)
        
        tokens_unicos = sorted(list(set(tokens)))
        # print(tokens_unicos)
        # print('\n')
        
        # Se crea la lista de [indice] = token
        self.lista_indice_token = {i: token for i, token in enumerate(tokens_unicos)}
        # print(self.lista_indice_token)
        # print('\n')
        
        # Se crea la lista de [token] = encoder
        self.lista_token_encoder = encoder.generarEncoded(tokens_unicos)
        # print(self.lista_token_encoder['<UNK>'])
        # print(self.lista_indice_token[42])
        # print(self.lista_token_encoder['<UNK>'])
    
    def dameToken(self, indice = None) -> str:
        if(indice in self.lista_indice_token): return self.lista_indice_token[indice]
        else: return self.TOKE_UNK
        
    def dameEncoder(self, token = "") -> np.ndarray:
        token = token.lower().strip()
        
        if(token in self.lista_token_encoder): 
            if(token == self.TOKE_PAD):
                # return np.asarray(self.lista_token_encoder[token])
                return np.zeros_like(self.lista_token_encoder[token])
            else:
                return np.array(self.lista_token_encoder[token])
        else: return np.array(self.lista_token_encoder[self.TOKE_UNK])
        
    def dameTokenEND(self) -> str:
        return self.TOKE_END
    
    def dameTokenPAD(self) -> str:
        return self.TOKE_PAD
    
    def dameTokenUNK(self) -> str:
        return self.TOKE_UNK
    
    def dameTokens(self) -> list:
        return self.tokens_originales
    