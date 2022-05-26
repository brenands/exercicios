nota = float(input('Digite a nota do aluno: '))
faltas = int(input('Digite o número de faltas: '))

if 9 >= nota <= 10:
    if faltas > 20:
        print('Conceito B')
    else:
        print('Conceito A')
elif 7.5 >= nota < 9:
    if faltas > 20:
        print('Conceito C')
    else:
        print('Conceito B')
elif 5 >= nota < 7.5:
    if faltas > 20:
        print('Conceito D')
    else:
        print('Conceito C')
elif 4 >= nota < 5:
    if faltas > 20:
        print('Conceito E')
    else:
        print('Conceito D')
else:
    print('Conceito E')
