import numpy as np

class OneHotEncoded:
    forma = ()
    lista_one_hot_encoded = {}
       
    def generarEncoded(self, tokens_unicos:list = []):    
        if(len(tokens_unicos) == 0): return self.lista_one_hot_encoded
        else:
            indices_tokens = {token: i for i, token in enumerate(tokens_unicos)}
            
            one_hot_encoded = np.zeros((len(indices_tokens), len(indices_tokens)))
            
            for i, token in enumerate(indices_tokens):
                indice = indices_tokens[token]
                one_hot_encoded[i, indice] = 1
                self.lista_one_hot_encoded[token] = np.asanyarray(one_hot_encoded[i])
                
            self.forma = one_hot_encoded.shape
            return self.lista_one_hot_encoded