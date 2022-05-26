def eh_bissexto(ano):
    div_ano4 = ano % 4
    div_ano400 = ano % 400
    div_ano100 = ano % 100

    return (div_ano4 == 0 and div_ano100 != 0) or div_ano400 == 0


data = input('Digite a data, separando a dia, '
             'mes e ano por barra (Dia/Mes/Ano): ').split("/")
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])

if ano > 0:
    if mes <= 12:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia > 31:
                print('Data incorreta.')
        elif mes == 2:
            if eh_bissexto(ano):
                if dia > 29:
                    print('Data incorreta.')
            else:
                if dia > 28:
                    print('Data incorreta.')
        else:
            if dia > 30:
                print('Data incorreta.')
    else:
        print('Data incorreta.')
else:
    print('Data incorreta.')
