# Melhore o jogo do Exercício 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 058 - JOGO DA ADIVINHAÇÃO V.2.0'))
print('-' * 100)

pc = randint(0, 10)
acertou = False
cont = 0

print('Acabei de pensar em um número entre 0 e 10.')

while not acertou:
    palpite = int(input('Digite seu palpite: '))
    if palpite == pc:
        acertou = True
    else:
        if palpite < pc:
            print('Mais...')
        elif palpite > pc:
            print('Menos...')
    cont += 1

if cont == 1:
    print('\nAcertou de primeira!!!')
else:
    print(f'\nAcertou com {cont} tentativas!')

print('-' * 100)

input('Pressione ENTER para sair...')
