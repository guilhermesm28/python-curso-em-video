# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 025 - PROCURANDO UMA STRING DENTRO DE OUTRA'))
print('-' * 100)

nome = str(input('Qual é seu nome completo? ')).strip()
print(f'Seu nome tem Silva? {"SILVA" in nome.upper()}')

print('-' * 100)

input('Pressione ENTER para sair...')
