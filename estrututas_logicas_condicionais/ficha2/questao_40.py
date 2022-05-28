custo_fabrica = float(input('Digite o custo de fábrica: '))

if custo_fabrica < 12000:
    custo_consumidor = custo_fabrica + (custo_fabrica * 0.05)
elif 12000 <= custo_fabrica <= 25000:
    custo_consumidor = custo_fabrica + (custo_fabrica * 0.1) + (custo_fabrica * 0.15)
else:
    custo_consumidor = custo_fabrica + (custo_fabrica * 0.15) + (custo_fabrica * 0.2)

print(f'Custo ao consumidor: R${custo_consumidor}')
