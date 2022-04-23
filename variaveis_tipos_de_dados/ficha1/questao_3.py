# num1 = int(input('Digite um numero: '))
# num2 = int(input('Digite um numero: '))
# num3 = int(input('Digite um numero: '))
#
# soma = num1 + num2 + num3
# print(f'A soma dos números é igual a {soma}.')

contagem = 0
soma_num = 0

while contagem < 3:
    num = int(input('Digite um numero: '))
    soma_num = num + soma_num
    contagem +=1

print(f'A soma dos números é igual a {soma_num}.')