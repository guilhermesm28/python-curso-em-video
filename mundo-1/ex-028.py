# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 028 - JOGO DA ADIVINHAÇÃO V.1.0'))
print('-' * 100)

print('Pensei em um número entre 0 e 5. Tente adivinhar...')

numero = randint(0, 5)

tentativa = int(input('Em qual número eu pensei? '))

print('PROCESSANDO...')

sleep(2)

if tentativa == numero:
    print('Parabéns! Você acertou o número que pensei!')
else:
    print(f'Errrrrrou! Pensei no número {numero}, não no {tentativa}...')

print('-' * 100)

input('Pressione ENTER para sair...')
