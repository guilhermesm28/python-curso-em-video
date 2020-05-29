# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 020 - SORTEANDO UMA ORDEM NA LISTA'))
print('-' * 100)

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

lista = [a1, a2, a3, a4]
shuffle(lista)

print(f'A ordem de apresentação será: {lista}')

print('-' * 100)

input('Pressione ENTER para sair...')
