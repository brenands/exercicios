def obter_dados():
    reta1 = float(input('Digite o primeiro lado do triangulo: '))
    reta2 = float(input('Digite o segundo lado do triangulo: '))
    reta3 = float(input('Digite o terceiro lado do triangulo: '))

    return reta1, reta2, reta3


def somar_lados(reta1, reta2, reta3):
    soma1_2 = reta1 + reta2
    soma1_3 = reta1 + reta3
    soma3_2 = reta3 + reta2

    return soma1_2, soma1_3, soma3_2


reta1, reta2, reta3 = obter_dados()
soma1_2, soma1_3, soma3_2 = somar_lados(reta1, reta2, reta3)

#verificação
while soma1_2 < reta3 or soma1_3 < reta2 or soma3_2 < reta1:
    print('O comprimento de um dos lados é maior'
          ' que a soma dos outros dois lados.')

    reta1, reta2, reta3 = obter_dados()
    soma1_2, soma1_3, soma3_2 = somar_lados(reta1, reta2, reta3)

#verificação
while reta1 < 0 or reta2 < 0 or reta3 < 0:
    print('O comprimento do lado não pode ser menor que zero.')

    reta1, reta2, reta3 = obter_dados()
    soma1_2, soma1_3, soma3_2 = somar_lados(reta1, reta2, reta3)

if reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
    print('Os lados escolhidos resultam '
          'em um triangulo escaleno.')

elif reta1 == reta2 and reta1 == reta3 and reta2 == reta3:
    print('Os lados escolhidos resultam '
          'em um triangulo equilatero.')

else:
    print('Os lados escolhidos resultam '
          'em um triangulo isósceles.')
