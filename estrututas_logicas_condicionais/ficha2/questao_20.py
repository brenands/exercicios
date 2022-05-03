reta1 = float(input('Digite o primeiro lado do triangulo: '))
reta2 = float(input('Digite o segundo lado do triangulo: '))
reta3 = float(input('Digite o terceiro lado do triangulo: '))

soma1_2 = reta1 + reta2
soma1_3 = reta1 + reta3
soma3_2 = reta3 + reta2

while soma1_2 < reta3 or soma1_3 < reta2 or soma3_2 < reta1:
    print('O comprimento de um dos lados é maior'
          ' que a soma dos outros dois lados.')
    reta1 = float(input('Digite o primeiro lado do triangulo: '))
    reta2 = float(input('Digite o segundo lado do triangulo: '))
    reta3 = float(input('Digite o terceiro lado do triangulo: '))

    soma1_2 = reta1 + reta2
    soma1_3 = reta1 + reta3
    soma3_2 = reta3 + reta2

while reta1 < 0 or reta2 < 0 or reta3 < 0:
    print('O comprimento do lado não pode ser menor que zero.')
    reta1 = float(input('Digite o primeiro lado do triangulo: '))
    reta2 = float(input('Digite o segundo lado do triangulo: '))
    reta3 = float(input('Digite o terceiro lado do triangulo: '))

    soma1_2 = reta1 + reta2
    soma1_3 = reta1 + reta3
    soma3_2 = reta3 + reta2

if reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
    print('Os lados escolhidos resultam '
          'em um triangulo escaleno.')

elif reta1 == reta2 and reta1 == reta3 and reta2 == reta3:
    print('Os lados escolhidos resultam '
          'em um triangulo equilatero.')

else:
    print('Os lados escolhidos resultam '
          'em um triangulo isósceles.')
