def somar(num1, num2):
    soma = num1 + num2
    return soma


def subtrair(num1, num2):
    if num1 > num2:
        subtracao = num1 - num2
        return subtracao
    else:
        subtracao = num2 - num1
        return subtracao


def multiplicar(num1, num2):
    multiplicacao = num1 * num2
    return multiplicacao


def dividir(num1, num2):
    if num2 != 0:
        divisao = num1 / num2
        return divisao


print('Digite (1) para soma de entre dois números.')
print('Digite (2) para subtração entre dois números.')
print('Digite (3) para multiplicação entre dois números.')
print('Digite (4) para divisão entre dois números.')

operacao = int(input('Qual operação matemática deseja utilizar? '))

while (operacao < 1 or operacao > 4):
    print('Digite (1) para soma de entre dois números.')
    print('Digite (2) para subtração entre dois números.')
    print('Digite (3) para multiplicação entre dois números.')
    print('Digite (4) para divisão entre dois números.')

    operacao = int(input('Qual operação mate'
                         'mática deseja utilizar? '))

num1 = float(input('Qual é o primeiro numero? '))
num2 = float(input('Qual é o segundo numero? '))

if operacao == 1:
    soma = somar(num1, num2)
    print(f'A soma é igual a {soma}.')

if operacao == 2:
    subtracao = subtrair(num1, num2)
    print(f'A subtração é igual a {subtracao}.')

if operacao == 3:
    multiplicacao = multiplicar(num1, num2)
    print(f'A multiplcação é igual a {multiplicacao}.')

if operacao == 4:
    divisao = dividir(num1, num2)
    print(f'A divisão é igual a {divisao}.')