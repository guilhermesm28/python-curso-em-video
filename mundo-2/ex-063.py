# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 063 - SEQUÊNCIA DE FIBONACCI V.1.0'))
print('-' * 100)

n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1

while n > 0:
    print(f'{t1} - ', end='')
    t1 += t2
    t2 = t1 - t2
    n -= 1

print('FIM!')

print('-' * 100)

input('Pressione ENTER para sair...')
