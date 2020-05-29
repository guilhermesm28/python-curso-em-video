# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 016 - QUEBRANDO UM NÚMERO'))
print('-' * 100)

num = float(input('Digite um número: '))

print(f'O número digitado foi {num} e sua porção inteira é {trunc(num)}')

print('-' * 100)

input('Pressione ENTER para sair...')
