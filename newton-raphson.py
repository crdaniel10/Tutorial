

# definir la función y su derivada

# Para f(x) = exp(-x) - x

import math

def f(x):
    return math.exp(-x) - x

def f_prime(x):
    return -math.exp(-x) - 1 


""" Para f(x) x**3 - x - 1

def f(x):
    return x**3 - x - 1

def f_prime(x):
    return 3 * x**2 - 1

"""

# Método Newton-Raphson

def newton_raphson(x0, epsilon, max_iterations):
    x = x0
    iteration = 0

    while abs(f(x)) > epsilon and iteration < max_iterations:
        x = x - f(x) / f_prime(x)
        iteration += 1

    if abs(f(x)) <= epsilon:
        return x
    else:
        return None

# Parámetros del método 66666666666

x0 = 1.0    #Valor inicial de x
epsilon =  1e-6     #Criterio de convergencia
max_iterations = 100 #Número máximo de iteraciones

# Ejecutar el método de Newton-Raphson

root = newton_raphson(x0, epsilon, max_iterations)

# Imprimir resultado

if root is not None:

    print("La raíz es:  ", root)
else:
    print("El método no converge o excede el número máximo de iteraciones.")





