
def divisor():
    for i in range(1, valor + 1):
        if valor % i == 0:
            print(f'{i}', end=' ')


# programa principal
valor = int(input('informe um valor inteiro e positivo -> '))
if valor > 0:
    divisor()
else:
    print('valor deve ser positivo')