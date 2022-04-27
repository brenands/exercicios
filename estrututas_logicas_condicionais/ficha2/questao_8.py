nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))

if nota2 and nota1 >= 0 and nota2 and nota1 <= 10:
    media = (nota1 + nota2) / 2
    print(f'A média das notas é igual a {media}.')

else:
    print(f'Os valores das notas não são válidos.')