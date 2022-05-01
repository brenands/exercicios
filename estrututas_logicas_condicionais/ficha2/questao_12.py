import math
num = int(input('Digite um número inteiro: '))
if num < 0:
    print('Número Inválido')
else:
    num_log = math.log(num, 10)
    print(num_log)
