import math

def train_test_split(X, y, test_size = 0.1):
    tamX, _ = X.shape
    tamY, _ = y.shape
    x_train = None
    y_train = None
    x_test = None
    y_test = None

    if(test_size != None):
        indiceFinal = math.ceil(tamX * test_size)
        x_train = X[:(tamX - indiceFinal + 1)]
        y_train = y[:(tamY - indiceFinal + 1)]
        x_test = X[(tamX - indiceFinal):]
        y_test = y[(tamY - indiceFinal):]
    else:
        x_train = X
        y_train = y
        x_test = X
        y_test = y

    return x_train, y_train, x_test, y_test