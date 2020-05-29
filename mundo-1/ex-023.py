# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 023 - SEPARANDO DÍGITOS DE UM NÚMERO'))
print('-' * 100)

num = int(input('Digite um número: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

print('-' * 100)

input('Pressione ENTER para sair...')
