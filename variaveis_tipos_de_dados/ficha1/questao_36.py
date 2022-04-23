import numpy

altura = float(input('Digite a altura do cilindro circular: '))
raio = float(input('Digite a raio do cilindro circular: '))
volume = numpy.pi * (raio ** 2) * altura

print(f'O volume do cilindro circular é igual a {volume}.')
