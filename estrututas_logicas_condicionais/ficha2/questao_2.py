import math
num = int(input('Digite um número: '))

if num >= 0:
    raiz = math.sqrt(num)
    print(f'A raiz de {num} é igual a {raiz}.')
else:
    print('Número invalido.')