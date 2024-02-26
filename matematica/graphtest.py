import numpy as np
import matplotlib.pyplot as plt

def exponencial_crescente(x):
    return np.exp(x)

def exponencial_decrescente(x):
    return np.exp(-x)

def funcao_negativa(x):
    return -2 * x


x = np.linspace(-5, 5, 1000)

# chamando as funcs
y_exp_crescente = exponencial_crescente(x)
y_exp_decrescente = exponencial_decrescente(x)
y_funcao_negativa = funcao_negativa(x)

# grafico
plt.figure()

plt.plot(x, y_exp_crescente, label='Exponencial Crescente')
plt.plot(x, y_exp_decrescente, label='Exponencial Decrescente')
plt.plot(x, y_funcao_negativa, label='Função Negativa')

#legenda
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.show()
