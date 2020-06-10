# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 065 - MÉDIA E MAIOR/MENOR VALOR'))
print('-' * 100)

continuar = 'S'
soma = cont = maior = menor = 0

while continuar == 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]

print(f'Média dos valores digitados: {soma / cont:.2f}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')

print('-' * 100)

input('Pressione ENTER para sair...')
