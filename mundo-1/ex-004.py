# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 004 - DISSECANDO UMA VARIÁVEL'))
print('-' * 100)

x = input('Digite algo: ')

print(f'Tipo primitivo: {type(x)}')
print(f'Só tem espaços? {x.isspace()}')
print(f'É um número? {x.isnumeric()}')
print(f'É alfabético? {x.isalpha()}')
print(f'É alfanumérico? {x.isalnum()}')
print(f'Está em maiúsculas? {x.isupper()}')
print(f'Está em minúsculas? {x.islower()}')
print(f'Está capitalizado? {x.istitle()}')

print('-' * 100)

input('Pressione ENTER para sair...')
