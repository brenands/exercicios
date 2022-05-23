print('Vamos resolver uma equação de segundo grau!')
a = float(input('Digite o valor de (a): '))
b = float(input('Digite o valor de (b): '))
c = float(input('Digite o valor de (c): '))

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print('Não existe raiz.')
elif delta == 0:
    x = (-b) / (2 * a)
    print(f'Como o delta é igual a zero, o valor da função é de {x}')
elif delta > 0:
    x1 = ((-b) + (delta ** 0.5)) / (2 * a)
    x2 = ((-b) - (delta ** 0.5)) / (2 * a)
    print(f'Como o delta é maior que zero, os valores da função são de {x1} e {x2}')