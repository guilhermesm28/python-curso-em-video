# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 012 - CALCULANDO DESCONTOS'))
print('-' * 100)

produto = float(input('Quanto custa o produto? R$ '))
desconto = produto * 5 / 100
novo_preco = produto - desconto

print(
    f'Com o desconto de 5% (R$ {desconto:.2f}), o produto que custava R$ {produto:.2f} passa a custar R$ {novo_preco:.2f}.')

print('-' * 100)

input('Pressione ENTER para sair...')
