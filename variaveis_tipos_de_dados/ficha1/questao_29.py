import numpy
contagem = 0
lista_nota = []

while contagem < 4:
    nota = float(input(f'Digite a {contagem+1}ª nota: '))
    lista_nota.append(nota)
    contagem +=1

media_notas = numpy.mean(lista_nota)
print(lista_nota[0])
print(f'A média dos números é igual a {media_notas}.')