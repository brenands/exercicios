def checar_nota(nota):
    while (nota < 0 or nota > 10):
        nota = float(input('Digite uma nota entre 0 e 10: '))
    return nota

nota_trab = checar_nota(float(input('Digite a primeira nota: ')))
nota_aval = checar_nota(float(input('Digite a segunda nota: ')))
nota_final = checar_nota(float(input('Digite a terceira nota: ')))
media = ((nota_trab * 2) + (nota_aval * 3) + (nota_final * 5)) / 10

if media < 3:
    print(f'A média foi de {media}, reprovado.')
elif media >= 3 and media < 5:
    print(f'A média foi de {media}, recuperação.')
else:
    print(f'A média foi de {media}, aprovado.')
