num = int(input('Digite um número inteiro maior que zero: '))
num_lista = str(num)
num_lista = list(num_lista)
# int(a) for a in str(num)
lista_int = list(map(int, num_lista))
print(lista_int)
soma = 0

if num > 0:
    for i in lista_int:
        soma += i
    print(soma)
else:
    print('Número inválido')