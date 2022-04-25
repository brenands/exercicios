premio = 780000

ganhador1 = premio * 0.46
formatado_g1 = f'{ganhador1:_.2f}'
formatado_g1 = formatado_g1.replace('.',',').replace('_','.')
ganhador2 = premio * 0.32
formatado_g2 = f'{ganhador2:_.2f}'
formatado_g2 = formatado_g2.replace('.',',').replace('_','.')
ganhador3 = premio * 0.22
formatado_g3 = f'{ganhador3:_.2f}'
formatado_g3 = formatado_g3.replace('.',',').replace('_','.')

print(f'O primeiro ganhador recebe R$ {formatado_g1}.')
print(f'O segundo ganhador recebe R$ {formatado_g2}.')
print(f'O terceiro ganhador recebe R$ {formatado_g3}.')