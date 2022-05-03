idade = int(input('Digite sua idade: '))
tempo_servico = int(input('Quantos anos têm de serviço? '))

diferenca = idade - tempo_servico

while idade < 0 or tempo_servico < 0:
    print('Informações inválidas.')
    idade = int(input('Digite sua idade: '))
    tempo_servico = int(input('Quantos anos têm de serviço? '))

while idade < 18 and tempo_servico >= 1:
    print('Proibido trabalhar sendo menor de idade.')
    idade = int(input('Digite sua idade: '))
    tempo_servico = int(input('Quantos anos têm de serviço? '))

while diferenca < 18 and tempo_servico >= 1:
    print('Não é póssivel ter todo esse tempo de trabalho '
          'com essa idade.')
    idade = int(input('Digite sua idade: '))
    tempo_servico = int(input('Quantos anos têm de serviço? '))

if (idade >= 65 or tempo_servico >= 30) or (idade >= 60 and tempo_servico >= 25):
    print('Você pode se aposentar.')

else:
    print('Você não pode se aposentar.')
