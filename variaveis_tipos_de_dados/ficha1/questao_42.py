salario_base = float(input('Digite seu salário atual: '))

gratificacao_salario = salario_base * 1.05
imposto_salario = salario_base * 0.07

salario_liquido = gratificacao_salario - imposto_salario
valor_formatado = f'R$ {salario_liquido:_.2f}'
valor_formatado = valor_formatado.replace('.',',').replace('_','.')

print(f'Voce receberá {valor_formatado}.')