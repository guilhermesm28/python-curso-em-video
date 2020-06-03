# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 050 - SOMA DOS PARES'))
print('-' * 100)

soma = 0
cont = 0

for i in range(1,7):
    n = int(input(f'{i}º valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
    
print(f'\nQuantidade de números pares: {cont} \nSoma dos números pares: {soma}')

print('-' * 100)

input('Pressione ENTER para sair...')
