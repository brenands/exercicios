def eh_bissexto(ano):
    div_ano4 = ano % 4
    div_ano400 = ano % 400
    div_ano100 = ano % 100

    return (div_ano4 == 0 and div_ano100 != 0) or div_ano400 == 0


ano = int(input('Digite um ano: '))

while ano < 0:
    print('Informações inválidas.')
    ano = int(input('Digite um ano: '))

if eh_bissexto(ano):
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} não é bissexto.')