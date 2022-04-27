num1 = int(input('Digite um numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 > num2:
    print(f'{num1} é maior que o {num2}.')
elif num1 == num2:
    print('Os números são iguais')
else:
    print(f'O {num2} é maior que o {num1}.')
