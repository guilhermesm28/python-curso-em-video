# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 027 - PRIMEIRO E ÚLTIMO NOME DE UMA PESSOA'))
print('-' * 100)

nome = str(input('Digite seu nome completo: ')).title().strip().split()

print(f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[-1]}')

print('-' * 100)

input('Pressione ENTER para sair...')
