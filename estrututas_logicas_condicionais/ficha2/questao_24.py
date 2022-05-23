valor = float(input('Digite o valor da compra: '))
estado = input('Digite em que estado a compra foi efetuada: ')
estado = str.upper(estado)

if estado != 'SP' and estado != 'MG' and estado != 'RJ' and estado != 'MS':
    print('O estado informado não foi cadastrado')

if estado == 'SP':
    valor_imposto = valor * 1.12
    print(f'O valor final do produto será de R$ {valor_imposto:.2f}.')
elif estado == 'MG':
    valor_imposto = valor * 1.07
    print(f'O valor final do produto será de R$ {valor_imposto:.2f}.')
elif estado == 'RJ':
    valor_imposto = valor * 1.15
    print(f'O valor final do produto será de R$ {valor_imposto:.2f}.')
elif estado == 'MS':
    valor_imposto = valor * 1.08
    print(f'O valor final do produto será de R$ {valor_imposto:.2f}.')


# mg = 7% ; sp = 12% ; rj = 15% ; ms = 8%