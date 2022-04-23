num = int(input('Digite um numero inteiro: '))

num_antes = num - 1
num_depois = num + 1
triplo_depois = num_depois ** 3
dobro_antes = num_antes ** 2

soma = triplo_depois + dobro_antes


print(f'A soma é igual a {soma}.')
