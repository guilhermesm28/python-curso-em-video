# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 010 - CONVERSOR DE MOEDAS'))
print('-' * 100)

reais = float(input('Quanto você tem em dinheiro? R$ '))
dolar_hoje = float(input('Qual a cotação do dólar hoje? $ '))

dolar = reais / dolar_hoje

print(f'Com {reais:.2f} reais, você pode comprar {dolar:.2f} dólares')

print('-' * 100)

input('Pressione ENTER para sair...')
