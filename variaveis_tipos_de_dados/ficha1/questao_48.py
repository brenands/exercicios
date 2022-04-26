num = int(input('Digite um número inteiro em segundos: '))

num_s = num
num_min = num / 60
num_h = num_min / 60

print(f'{num_h} h.')
print(f'{num_min} min.')
print(f'{num_s} s.')