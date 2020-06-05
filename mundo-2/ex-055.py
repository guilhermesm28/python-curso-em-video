# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 055 - MAIOR E MENOR DA SEQUÊNCIA'))
print('-' * 100)

maior = 0
menor = 0

for i in range(1,6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'\nMaior peso: {maior:.2f}kg \nMenor peso: {menor:.2f}kg')

print('-' * 100)

input('Pressione ENTER para sair...')
