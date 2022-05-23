print('Vamos resolver a média dos números!')

a = int(input('Digite o valor de (a): '))
b = int(input('Digite o valor de (b): '))
c = int(input('Digite o valor de (c): '))


print('Digite (1) para média geométrica')
print('Digite (2) para média ponderada')
print('Digite (3) para média harmônica')
print('Digite (4) para média aritmética')
escolha = int(input('Qual tipo de média deseja realizar? '))

if escolha == 1:
    media = (a * b * c) ** (1/3)
    print(media)
elif escolha == 2:
    media = (a + (2 * b) + (3 * c)) / 6
    print(media)
elif escolha == 3:
    media = 1 / ((1/a) + (1/b) + (1/c))
    print(media)
elif escolha == 4:
    media = (a + b + c) / 3
    print(media)
else:
    print('O valor digitado não pe válido.')
