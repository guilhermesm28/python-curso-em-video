# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 052 - NÚMEROS PRIMOS'))
print('-' * 100)

n = int(input('Digite um número: '))

cont = 0

for i in range(1, n + 1):
    if n % i == 0:
        cont += 1

print(f'\nO número {n} foi divisível {cont} vezes.')

if cont == 2:
    print('É um número primo!')
else:
    print('Não é um número primo!')

print('-' * 100)

input('Pressione ENTER para sair...')
