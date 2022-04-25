valor_hora = float(input('Digite o valor da hora de trabalho: '))
horas_trabalhados = int(input('Digite o número de horas trabalhadas: '))
salario = valor_hora * horas_trabalhados * 1.1
valor_formatado = f'R$ {salario:_.2f}'
valor_formatado = valor_formatado.replace('.',',').replace('_','.')

print(f'Voce receberá {valor_formatado}.')
