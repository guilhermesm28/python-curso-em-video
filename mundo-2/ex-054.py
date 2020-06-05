# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 054 - GRUPO DA MAIORIDADE'))
print('-' * 100)

hoje = date.today().year
maior = 0

for i in range(1,8):
    nasc = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    idade = hoje - nasc
    if idade >= 18:
        maior += 1

print(f'\nMaiores de idade: {maior} \nMenores de idade: {7 - maior}')

print('-' * 100)

input('Pressione ENTER para sair...')
