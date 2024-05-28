import numpy as np
from App.Util.FuncionesActivacion import *

x_t = np.asanyarray([
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
])
n_x, m = x_t.shape
n_a = 1

a_prev = np.zeros((n_a, m))
c_prev = np.zeros((n_a, m))
w_f = np.zeros((n_a, n_x + n_a))
b_f = np.zeros((n_a, 1))

print(f"n_x: {x_t.shape[0]}, m: {x_t.shape[1]}")
print(f"n_a: {a_prev.shape[0]}, m: {a_prev.shape[1]}")
print(x_t)
print(a_prev)
print(w_f)
print(b_f)
print('----------------------')

concat = np.concatenate((a_prev, x_t), axis=0)
print(concat)
ft = softmax(w_f @ concat + b_f)
print(ft)

# x = np.array([[1, 0, 1, 1],
#               [1, 1, 0, 1]])
# wy = np.array([[1, 1],
#                [2, 2]])
# by = np.array([[1]])
# y = wy @ x + by