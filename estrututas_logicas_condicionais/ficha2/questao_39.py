salario_atual = float(input('Digite o seu salário: '))
tempo_servico = int(input('Digite o tempo de empresa: '))

if salario_atual < 500:
    salario_atual = salario_atual * 1.25
elif 500 < salario_atual < 1000:
    salario_atual = salario_atual * 1.20
elif 1000 < salario_atual < 1500:
    salario_atual = salario_atual * 1.15
elif 1500 < salario_atual < 2000:
    salario_atual = salario_atual * 1.10
else:
    print('Sem reajuste.')

if tempo_servico < 1:
    print('Sem bônus.')
elif 1 <= tempo_servico <= 3:
    salario_atual = salario_atual + 100
elif 4 <= tempo_servico <= 6:
    salario_atual = salario_atual + 200
elif 7 <= tempo_servico <= 10:
    salario_atual = salario_atual + 300
else:
    salario_atual = salario_atual + 500

print(f'Salário reajustado: R$ {salario_atual}')