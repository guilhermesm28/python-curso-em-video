# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 060 - CÁLCULO DE FATORIAL'))
print('-' * 100)

n = int(input('Digite um número: '))
c = n
f_while = 1
f_for = 1

while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f_while *= c
    c -= 1

print(f'{f_while} - Laço WHILE')

for i in range(n, 0, -1):
    print(f'{i}', end='')
    print(f' x ' if i > 1 else ' = ', end='')
    f_for *= i

print(f'{f_for} - Laço FOR')

print('-' * 100)

input('Pressione ENTER para sair...')
