import numpy as np

# -----------------------------------------------
# Funciones de activación para la capa de salida
# -----------------------------------------------

def linear(z: np.ndarray, derivative=False):
    a = z
    if derivative:
        da = np.ones(z.shape)
        return a, da
    return a


def logistic(z: np.ndarray, derivative=False):
    a = 1/(1 + np.exp(-z))
    if derivative:
        da = np.ones(z.shape)
        return a, da
    return a


def softmax(z: np.ndarray, derivative=False):
    e = np.exp(z - np.max(z))
    a = e / np.sum(e)
    if derivative:
        da = np.ones(z.shape)
        return a, da
    return a

# -----------------------------------------------
# Funciones de activación para la capa oculta
# -----------------------------------------------

def tanh(z: np.ndarray, derivative=False):
    a = np.tanh(z)
    if derivative:
        da = (1 - a) * (1 + a)
        return a, da
    return a


def relu(z: np.ndarray, derivative=False):
    a = z * (z >= 0)
    if derivative:
        da = np.array(z >= 0, dtype=float)
        return a, da
    return a

def logistic_hidden(z: np.ndarray, derivative=False):
    a = 1/(1 + np.exp(-z))
    if derivative:
        da = a * (1 - a)
        return a, da
    return a