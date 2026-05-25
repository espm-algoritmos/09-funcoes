
def validar() -> bool:
    return lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2

def classificar():
    if lado1 == lado2 and lado1 == lado3:
        print('equilátero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('isósceles')
    else:
        print('escaleno')

# programa principal
lado1 = int(input('lado 1 --> '))
lado2 = int(input('lado 2 --> '))
lado3 = int(input('lado 3 --> '))
if validar():
    classificar()
else:
    print('os valores não formam um triângulo')