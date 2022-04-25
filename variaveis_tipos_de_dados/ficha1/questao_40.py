diaria = 30
desconto = 1.08

dias_trabalhados = int(input('Digite a quantidade de dias do serviço: '))
valor_liquido = (diaria * dias_trabalhados) * desconto
valor_formatado = f'R$ {valor_liquido:_.2f}'
valor_formatado = valor_formatado.replace('.',',').replace('_','.')

print(f'Você receberá {valor_formatado}.')
# encanador recebe 30 conto por dia
# perguntar quantos dias ele vai trabalhar
# descontar 8% de imposto de renda
