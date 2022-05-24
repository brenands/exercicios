import random


def somar():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    soma = int(input(f'Qual a soma entre {num1} e {num2}? '))

    return soma == num1 + num2


acertos = 0
erros = 0
vezes = 0

while vezes < 5:
    acertou = somar()
    if acertou:
        print('Resposta correta!')
        acertos += 1
    else:
        erros += 1
    vezes += 1

print(f'Você acertou {acertos} perguntas.')
print(f'Você errou {erros} perguntas.')
