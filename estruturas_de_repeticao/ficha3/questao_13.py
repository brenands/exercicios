contagem = 0
numero = int(input('Digite um numéro par: '))
if numero % 2 == 0:
    while contagem <= numero:
        print(contagem)
        contagem += 2
else:
    print('O numéro não é par.')