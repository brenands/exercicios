import math

num = float(input('Digite um numero real: '))
if num >= 0:
    raiz = math.sqrt(num)
    print(f'A raiz quadrada de {num} é igual a {raiz}.')

else:
    quadrado = num ** 2
    print(f'O {num} ao quadrado é igual a {quadrado}.')