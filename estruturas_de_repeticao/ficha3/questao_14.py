numero = int(input('Digite um numéro par: '))
contagem = numero
if numero % 2 == 0:
    while contagem >= 0:
        print(contagem)
        contagem -= 2
else:
    print('O numéro não é par.')