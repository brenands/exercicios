altura = float(input('Digite a altura: '))
peso = float(input('Digite o peso: '))

if altura < 1.20:
    if peso < 60:
        print('Classe A')
    elif peso >= 60 and peso <= 90:
        print('Classe D')
    else:
        print('Classe G')
elif altura >= 1.20 and altura <= 1.70:
    if peso < 60:
        print('Classe B')
    elif peso >= 60 and peso <= 90:
        print('Classe E')
    else:
        print('Classe H')
else:
    if peso < 60:
        print('Classe C')
    elif peso >= 60 and peso <= 90:
        print('Classe F')
    else:
        print('Classe I')