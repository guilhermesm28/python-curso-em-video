# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 002 - RESPONDENDO AO USUÁRIO'))
print('-' * 100)

nome = input('Digite seu nome: ')

print(f'Bem-vindo, {nome}!')

print('-' * 100)

input('Pressione ENTER para sair...')
