import re

LECTURA = 'r'
UTF_8 = 'utf-8'

def generarTokens(ruta_documento = None, exp_regular = None, esDocumento = True):
    tokens = []
    if(ruta_documento and exp_regular):
        if(esDocumento):
            with open(ruta_documento, LECTURA, encoding=UTF_8) as archivo:
                documento = archivo.read()
        else: documento = ruta_documento
        
        tokens = re.sub(exp_regular, ' ', documento.lower().strip())
        tokens = re.findall(r'\b\w+\b|[^\w\s]', tokens)
        tokens = [token for token in tokens if token != '']

        return tokens
    else: return tokens