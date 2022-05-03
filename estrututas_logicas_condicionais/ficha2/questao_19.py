num = int(input('Digite um número inteiro: '))

num_div3 = num % 3
num_div5 = num % 5

if num_div3 == 0:
    print(f'O número {num} é divisível por 3.')
else:
    print(f'O número {num} não é divisível por 3.')

if num_div5 == 0:
    print(f'O número {num} é divisível por 5.')
else:
    print(f'O número {num} não é divisível por 5.')