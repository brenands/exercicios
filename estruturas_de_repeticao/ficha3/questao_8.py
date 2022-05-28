contagem = 0
maior_valor = 0
menor_valor = 0
while contagem < 10:
    valor = float(input('Digite um valor: '))
    if valor >= maior_valor:
        maior_valor = valor
    elif valor <= menor_valor:
        menor_valor = valor
    contagem += 1
print(f'Maior valor: {maior_valor}')
print(f'Menor valor: {menor_valor}')