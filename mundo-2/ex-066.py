# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 066 - VÁRIOS NÚMEROS COM FLAG'))
print('-' * 100)

soma = cont = 0

while True:
    n = int(input('Digite outro número [999 para sair]: '))
    if n == 999:
        break
    soma += n
    cont += 1

if n == 999 and cont <= 1:
    print('FIM!')
else:
    print(f'\nVocê digitou {cont} números. \nA soma entre eles é {soma}!')

print('-' * 100)

input('Pressione ENTER para sair...')
