# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 007 - MÉDIA ARITMÉTICA'))
print('-' * 100)

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

print(f'Média: {media:.2f}')

print('-' * 100)

input('Pressione ENTER para sair...')
