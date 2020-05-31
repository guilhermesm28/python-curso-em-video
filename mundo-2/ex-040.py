# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 040 - CLÁSSICO DA MÉDIA'))
print('-' * 100)

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print(f'Média: {media}\nVocê está REPROVADO!')
elif media >= 5.0 and media <= 6.9:
    print(f'Média: {media}\nVocê está de RECUPERAÇÃO!')
elif media >= 7.0 and media <= 10.0:
    print(f'Média: {media}\nVocê está APROVADO!')
else:
    print('Valores incorretos!')

print('-' * 100)

input('Pressione ENTER para sair...')
