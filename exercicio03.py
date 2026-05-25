
def maior() -> int:
    if valor1 > valor2 and valor1 > valor3:
        return valor1
    elif valor2 > valor3:
        return valor2
    return valor3

# programa principal
valor1 = int(input('digite o primeiro valor -> '))
valor2 = int(input('digite o segundo valor -> '))
valor3 = int(input('digite o terceiro valor -> '))
print(f'maior valor digitado: {maior()}')