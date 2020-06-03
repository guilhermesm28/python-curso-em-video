# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 048 - SOMA DE ÍMPARES MÚLTIPLOS DE 3'))
print('-' * 100)

soma = 0
cont = 0

for i in range(1,501,2):
    if i % 3 == 0:
        soma += i
        cont += 1

print(f'A soma de todos os {cont} valores solicitados é {soma}')

print('-' * 100)

input('Pressione ENTER para sair...')
