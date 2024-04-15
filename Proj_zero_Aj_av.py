import numpy as np
from scipy.optimize import curve_fit

# Dados fornecidos
x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
y = np.array([0.0, 0.5, 2.0, 4.5, 8.1, 12.3, 17.8, 24.8, 32.5, 41.3])


# Definindo as funções propostas
def func1(x, a0, a1, a2, a3):
    return a0 + a1 * x + a2 * x**2 + a3 * x**3


def func2(x, b0, b1, b2):
    return x * (b0 + b1 * x + b2 * x**2)


def func3(x, c0, c1):
    return x**2 * (c0 + c1 * x)


# Ajustando os parâmetros das funções aos dados
params1, _ = curve_fit(func1, x, y)
params2, _ = curve_fit(func2, x, y)
params3, _ = curve_fit(func3, x, y)

# Coeficientes das funções ajustadas
a0, a1, a2, a3 = params1
b0, b1, b2 = params2
c0, c1 = params3

# Calculando os valores previstos para cada função ajustada
predicted_y1 = func1(x, a0, a1, a2, a3)
predicted_y2 = func2(x, b0, b1, b2)
predicted_y3 = func3(x, c0, c1)

# Calculando os vetores de resíduos para cada função ajustada
residuals1 = y - predicted_y1
residuals2 = y - predicted_y2
residuals3 = y - predicted_y3

print("Coeficientes da função u(x) = a0 + a1*x + a2*x^2 + a3*x^3:")
print("a0 =", a0)
print("a1 =", a1)
print("a2 =", a2)
print("a3 =", a3)
print()

# Imprimindo os vetores de resíduos
print("Vetor de resíduos da função u(x) = a0 + a1*x + a2*x^2 + a3*x^3:")
print(residuals1)
print()

print("Coeficientes da função u(x) = x(b0 + b1*x + b2*x^2):")
print("b0 =", b0)
print("b1 =", b1)
print("b2 =", b2)
print()

print("Vetor de resíduos da função u(x) = x(b0 + b1*x + b2*x^2):")
print(residuals2)
print()

print("Coeficientes da função u(x) = x^2(c0 + c1*x):")
print("c0 =", c0)
print("c1 =", c1)
print()

print("Vetor de resíduos da função u(x) = x^2(c0 + c1*x):")
print(residuals3)
