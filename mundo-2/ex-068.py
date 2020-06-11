# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

from random import randint

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 068 - JOGO DO PAR OU ÍMPAR'))
print('-' * 100)

cont = 0

while True:
    n = 11 
    while n > 10:
        n = int(input('Digite um número: '))

    pc = randint(0,10)
    total = (n + pc)
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
        
    print(f'\n{n} + {pc} = {total} -> ', end='')
    print(f'PAR' if total % 2 == 0 else 'ÍMPAR')
    
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...\n')
    
if cont > 1:
    print(f'\nGAME OVER! Você venceu {cont} vezes!')
elif cont == 1:
    print('\nGAME OVER! Você venceu 1 vez!')
else:
    print('\nGAME OVER! Você não ganhou nenhuma vez!')
    
print('-' * 100)

input('Pressione ENTER para sair...')
