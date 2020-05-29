# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 019 - SORTEANDO UM ITEM NA LISTA'))
print('-' * 100)

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

lista = [a1, a2, a3, a4]
escolhido = choice(lista)

print(f'O aluno escolhido foi {escolhido}')

print('-' * 100)

input('Pressione ENTER para sair...')
