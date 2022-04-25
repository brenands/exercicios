valor_total = float(input('Digite o valor total: '))

desconto_10 = valor_total * 0.9
valor_formatado_d10 = f'R$ {desconto_10:_.2f}'
valor_formatado_d10 = valor_formatado_d10.replace('.',',').replace('_','.')

parcela_3x = valor_total / 3
valor_formatado_3x = f'R$ {parcela_3x:_.2f}'
valor_formatado_3x = valor_formatado_3x.replace('.',',').replace('_','.')

comissao_avista = desconto_10 * 0.05
valor_formatado_cavista = f'R$ {comissao_avista:_.2f}'
valor_formatado_cavista = valor_formatado_cavista.replace('.',',').replace('_','.')

comissao_aprazo = valor_total * 0.05
valor_formatado_caprazo = f'R$ {comissao_aprazo:_.2f}'
valor_formatado_caprazo = valor_formatado_caprazo.replace('.',',').replace('_','.')

print(f'Valor a vista: {valor_formatado_d10}.')
print(f'Valor da parcela em 3 vezes: {valor_formatado_3x}.')
print(f'Valor da comissão, caso compra a vista: {valor_formatado_cavista}.')
print(f'Valor da comissão, caso compra a prazo: {valor_formatado_caprazo}.')