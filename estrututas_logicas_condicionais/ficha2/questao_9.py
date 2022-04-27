salario = float(input('Digite o seu salário: '))
emprestimo = float(input('Digite o valor da prestação do empréstimo: '))

check_emprestimo = salario * 0.2

if check_emprestimo >= emprestimo:
    print('Empréstimo concedido.')

else:
    print('Empréstimo não consedido.')