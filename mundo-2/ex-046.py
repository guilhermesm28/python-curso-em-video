# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 046 - CONTAGEM REGRESSIVA'))
print('-' * 100)

for i in range(10,-1,-1):
    print(i)
    sleep(1)

print('BOOM! BOOM! POW! KABLAUM!')

print('-' * 100)

input('Pressione ENTER para sair...')
