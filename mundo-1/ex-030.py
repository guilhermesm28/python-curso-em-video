# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 030 - PAR OU ÍMPAR?'))
print('-' * 100)

n = int(input('Digite um número inteiro qualquer: '))

if n % 2 == 0:
    print('Esse número é PAR!')
else:
    print('Esse número é ÍMPAR!')
    
print('-' * 100)

input('Pressione ENTER para sair...')
