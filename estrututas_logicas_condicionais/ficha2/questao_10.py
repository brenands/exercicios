altura = float(input('Digite a sua altura: '))
sexo = input('Digite o seu sexo (M ou H): ')
sexo = sexo.upper()

if sexo == 'M':
    peso = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é igual a {peso}.')
elif sexo == 'H':
    peso = (72.7 * altura) - 58
    print(f'Seu peso ideal é igual a {peso}.')
else:
    print('Valores informados não são válidos.')
