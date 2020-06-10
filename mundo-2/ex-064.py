# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 064 - TRATANDO VÁRIOS VALORES V.1.0'))
print('-' * 100)

n = soma = cont = 0

while n != 999:
    n = int(input('Digite outro número [999 para sair]: '))
    if n != 999:
        soma += n
        cont += 1

if n == 999 and cont <= 1:
    print('FIM!')
else:
    print(f'\nVocê digitou {cont} números. \nA soma entre eles é {soma}!')

print('-' * 100)

input('Pressione ENTER para sair...')
