
from math import sqrt

def calcular_delta() -> float:
    return b ** 2 - 4 * a * c

def calcular_raiz():
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    return x1, x2

# programa principal
a = float(input('informe o valor de a --> '))
if a == 0:
    print('não é uma equação do 2o grau')
else:
    b = float(input('informe o valor de b --> '))
    c = float(input('informe o valor de c --> '))
    delta = calcular_delta()
    if delta < 0:
        print('a equação não tem raiz real')
    else:
        x1, x2 = calcular_raiz()
        print(f'x1 = {x1:.2f}')
        print(f'x2 = {x2:.2f}')