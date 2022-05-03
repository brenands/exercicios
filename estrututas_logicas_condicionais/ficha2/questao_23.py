ano = int(input('Digite um ano: '))

while ano < 0:
    print('Informações inválidas.')
    ano = int(input('Digite um ano: '))

div_ano = ano % 4

if div_ano == 0:
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} não é bissexto.')