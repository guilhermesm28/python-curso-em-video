# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 067 - TABUAVA V.3.0'))
print('-' * 100)

while True:
    n = int(input('\nQuer ver a tabuadade qual valor? '))
    if n < 0:
        break
    for i in range(1,11):
        print(f'{n} x {i:2} = {n*i:2}')

print('FIM!')

print('-' * 100)

input('Pressione ENTER para sair...')
