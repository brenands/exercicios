import math

num = float(input('Digite um numero real: '))
if num >= 0:
    raiz = math.sqrt(num)
    quadrado = num ** 2

    print(f'A raiz quadrada de {num} é igual a {raiz}.')
    print(f'O {num} ao quadrado é igual a {quadrado}.')

else:
    print('Número invalido.')