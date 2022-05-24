import random

def somar():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    soma = int(input(f'Qual a soma entre {num1} e {num2}? '))
    acertou = 0
    errou = 0
    if soma == (num1 + num2):
        acertou = 1
    else:
        errou = 1
    return acertou, errou


acertos = 0
erros = 0
vezes = 0

while vezes < 5:
    acertou, errou = somar()
    if acertou == 1:
        print('Resposta correta!')
    acertos += acertou
    erros += errou
    vezes += 1

print(f'Você acertou {acertos} perguntas.')
print(f'Você errou {erros} perguntas.')
