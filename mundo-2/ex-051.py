# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 051 - PROGRESSÃO ARITMÉTICA'))
print('-' * 100)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + 10 * razao

for i in range(termo, decimo, razao):
    print(i, end=' -> ')

print('ACABOU!')

print('-' * 100)

input('Pressione ENTER para sair...')
