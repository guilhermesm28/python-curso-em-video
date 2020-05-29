# Crie um programa que leia dois números e mostre a soma entre eles.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 003 - SOMANDO DOIS NÚMEROS'))
print('-' * 100)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

soma = n1 + n2

print(f'A soma entre "{n1}" e "{n2}" é igual a {soma}!')

print('-' * 100)

input('Pressione ENTER para sair...')
