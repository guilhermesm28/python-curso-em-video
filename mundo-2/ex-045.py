# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 045 - PEDRA, PAPEL E TESOURA'))
print('-' * 100)

print('Opções:\n[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESOURA')

eu = int(input('Escolha uma opção: '))

opcao = ['PEDRA','PAPEL','TESOURA']
pc = randint(0,2)

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)

if eu > 2:
    print('\nOpção inválida! Jogo encerrado!')
else:
    if (eu == 0 and pc == 1) or (eu == 1 and pc == 2) or (eu == 2 and pc == 0):
        print(f'\nCOMPUTADOR VENCEU! \nMinha jogada: {opcao[eu]} \nJogada do computador: {opcao[pc]}')
    elif eu == pc:
        print(f'\nEMPATE! \nMinha jogada: {opcao[eu]} \nJogada do computador: {opcao[pc]}')
    else:
        print(f'\nJOGADOR VENCEU! \nMinha jogada: {opcao[eu]} \nJogada do computador: {opcao[pc]}')

print('-' * 100)

input('Pressione ENTER para sair...')
