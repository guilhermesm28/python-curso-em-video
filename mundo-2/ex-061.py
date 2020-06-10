# Refaça o Exercício 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 061 - PROGRESSÃO ARITMÉTICA V.2.0'))
print('-' * 100)

p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

cont = 0

while cont < 10:
    print(f'{p1} - ', end='')
    p1 += r
    cont += 1

print('FIM!')

print('-' * 100)

input('Pressione ENTER para sair...')
