horas = input('Digite o horario exato, separando a hora,'
              ' minuto e segundos por backspace (Hora min seg): ').split(" ")
hora = int(horas[0])
min = int(horas[1])
seg = int(horas[2])

horas_exp = input('Digite o tempo total do experimento, separando a hora, '
                  'minuto e segundos por backspace (Hora min seg): ').split(" ")
hora_exp = int(horas_exp[0])
min_exp = int(horas_exp[1])
seg_exp = int(horas_exp[2])

soma_seg = seg + seg_exp
soma_min = min + min_exp
soma_hora = hora + hora_exp
dias = 0

if soma_seg >= 60:
    soma_seg -= 60
    soma_min += 1

if soma_min >= 60:
    soma_min -= 60
    soma_hora += 1

if soma_hora >= 24:
    dias = int(soma_hora / 24)
    soma_hora -= 24 * dias

if dias == 0:
    print(f'O experimento terminará hoje às {soma_hora}:{soma_min}:{soma_seg}')
elif dias == 1:
    print(f'O experimento terminará daqui a um dia {soma_hora}:{soma_min}:{soma_seg}')
else:
    print(f'O experimento terminará daqui a {dias} dias às {soma_hora}:{soma_min}:{soma_seg}')
