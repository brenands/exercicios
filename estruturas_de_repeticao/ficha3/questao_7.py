contagem = 0
valor_total = 0
while contagem < 10:
    valor = float(input('Digite um valor: '))
    if valor > 0:
        valor_total += valor
    contagem += 1
print(valor_total/10)