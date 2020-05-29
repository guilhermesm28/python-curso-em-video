# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 015 - ALUGUEL DE CARROS'))
print('-' * 100)

qtd_km = float(input('Quantos km rodados? '))
qtd_dias = int(input('Quantos dias alugados? '))

preco = (qtd_dias * 60) + (qtd_km * 0.15)

print(f'O total a pagar é R$ {preco:.2f}')

print('-' * 100)

input('Pressione ENTER para sair...')
