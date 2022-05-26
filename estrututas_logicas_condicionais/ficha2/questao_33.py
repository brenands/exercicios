preco_antigo = float(input('Digite o valor'))

if preco_antigo < 50:
    novo_preco = preco_antigo * 1.05
elif 50 <= preco_antigo <= 100:
    novo_preco = preco_antigo * 1.1
else:
    novo_preco = preco_antigo * 1.15

if novo_preco <= 80:
    print('Barato')
elif 80 < novo_preco <= 120:
    print('Normal')
elif 120 < novo_preco <= 200:
    print('Caro')
else:
    print('Muito caro')
