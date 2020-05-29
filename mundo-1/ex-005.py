# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 005 - ANTECESSOR E SUCESSOR'))
print('-' * 100)

n = int(input('Digite um número: '))

print(f'Antecessor: {n-1}')
print(f'Sucessor: {n+1}')

print('-' * 100)

input('Pressione ENTER para sair...')
