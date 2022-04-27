num1 = int(input('Digite um numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 > num2:
    print(f'{num1} é maior que o {num2}.')
    print(f'A diferença entre eles é {num1 - num2}.')
elif num1 == num2:
    print('Os números são iguais.')
    print(f'A diferença entre eles é {num1 - num2}.')
else:
    print(f'O {num2} é maior que o {num1}.')
    print(f'A diferença entre eles é {num2 - num1}.')

