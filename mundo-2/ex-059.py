# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 059 - MENU DE OPÇÕES'))
print('-' * 100)

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

while True:
    print('\n[ 1 ] Somar \n[ 2 ] Multiplicar \n[ 3 ] Maior \n[ 4 ] Digitar outros números \n[ 5 ] Sair do programa\n')
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif opcao == 2:
        print(f'{n1} x {n2} = {n1*n2}')  
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior número é {n1}!') 
        elif n1 < n2:
            print(f'O maior número é {n2}!')
        else:
            print(f'Os números {n1} e {n2} são iguais!')
    elif opcao == 4:
        print('\nDigite os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        break
    else:
        print(f'Opção inválida!')
    sleep(2)

print('Finalizado!')

print('-' * 100)

input('Pressione ENTER para sair...')
