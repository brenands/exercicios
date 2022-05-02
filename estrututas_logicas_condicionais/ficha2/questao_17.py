def checar_valor(valor):
    while (valor <= 0):
        print('O valor deve ser maior que zero.')
        valor = float(input('Qual a base maior do trapézio?' ))
    return valor

base_maior = checar_valor(float(input('Qual a base maior do trapézio? ')))
base_menor = checar_valor(float(input('Qual a base menor do trapézio? ')))
altura = checar_valor(float(input('Qual a altura do trapézio? ')))

area = (base_maior + base_menor) * altura / 2

print(f'A área do trapézio é igual a {area}.')
