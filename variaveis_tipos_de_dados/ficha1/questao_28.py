contagem = 0
soma_quad = 0

while contagem < 3:
    num = int(input('Digite um numero: '))
    quad = num ** 2
    soma_quad = quad + soma_quad
    contagem +=1

print(f'A soma dos números é igual a {soma_quad}.')