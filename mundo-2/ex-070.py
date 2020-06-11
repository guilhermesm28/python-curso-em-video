# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 070 - ESTATÍSTICAS EM PRODUTOS'))
print('-' * 100)

total = cont = barato = 0

while True:
    produto = str(input('Nome do produto: ')).strip().title()
    preco = float(input('Preço: R$ '))

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\nContinuar? [S/N] ')).strip().upper()[0]

    if total == 0 or preco < barato:
        barato = preco
        nome = produto
    if preco > 1000:
        cont += 1

    total += preco

    if continuar == 'N':
        break

print(f'Total: R$ {total:.2f}')
print(f'Produtos que custam mais de R$ 1000: {cont}')
print(f'Produto mais barato: {nome} -> R$ {barato:.2f}')
    
print('-' * 100)

input('Pressione ENTER para sair...')
