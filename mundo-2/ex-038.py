# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 038 - COMPARANDO NÚMEROS'))
print('-' * 100)

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print('O PRIMEIRO valor é maior!')
elif n1 < n2:
    print('O SEGUNDO valor é maior!')
else:
    print('Não existe valor maior, os dois são iguais!')

print('-' * 100)

input('Pressione ENTER para sair...')
