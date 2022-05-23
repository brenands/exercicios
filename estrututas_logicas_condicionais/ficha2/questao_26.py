distancia = float(input('Digite a distância percorrida: '))
litros_consumidos = float(input('Digite quantos litros foram consumidos: '))

autonomia = distancia / litros_consumidos

if autonomia < 8:
    print('Venda o carro!')
elif autonomia >= 8 and autonomia <= 12:
    print('Econômico!')
else:
    print('Muito econômico!')