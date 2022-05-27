hora_chegada = input('Digite a hora de chegada (HH:MM): ').split(":")
hora_saida = input('Digite a hora de saida (HH:MM): ').split(":")

hrs_chegada = int(hora_chegada[0])
min_chegada = int(hora_chegada[1])

hrs_saida = int(hora_saida[0])
min_saida = int(hora_saida[1])


if min_saida < min_chegada:
    hora_saida -= 1
    min_total = min_chegada - min_saida
else:
    min_total = min_saida - min_chegada

if hrs_saida < hrs_chegada:
    hrs_saida = hrs_saida + 24
    hrs_total = hrs_saida - hrs_chegada
else:
    hrs_total = hrs_saida - hrs_chegada

if hrs_total == 0 or hrs_total == 1:
    valor = (hrs_total + 1) * 1
    print(f'Preço cobrado R$ {valor:.2f}.')

elif hrs_total == 2 or hrs_total == 3:
    valor = (hrs_total + 1) * 1.4
    print(f'Preço cobrado R$ {valor:.2f}.')

else:
    valor = (hrs_total + 1) * 2
    print(f'Preço cobrado R$ {valor:.2f}.')
