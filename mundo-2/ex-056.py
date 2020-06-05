# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 056 - ANALISADOR COMPLETO'))
print('-' * 100)

soma = 0
idade_velho = 0
nome_velho = ''
qtd_f_menor = 0
feminino = 0

for i in range(1,5):
    print(f'\n{i}ª pessoa')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()
    soma += idade
    if i == 1 and sexo[:1] == 'M':
        idade_velho = idade
        nome_velho = nome
    if idade > idade_velho and sexo[:1] == 'M':
        idade_velho = idade
        nome_velho = nome
    if sexo[:1] == 'F' and idade < 20:
        qtd_f_menor += 1
        feminino = 1

media = soma / 4

print(f'\nA média de idade do grupo é {media:.2f}!')

if nome_velho != '':
    print(f'O homem mais velho é o {nome_velho}, com {idade_velho} anos!')

if feminino == 1:
    if qtd_f_menor == 1:
        print(f'{qtd_f_menor} mulher tem menos de 20 anos!')
    else:
        print(f'{qtd_f_menor} mulheres têm menos de 20 anos!')

print('-' * 100)

input('Pressione ENTER para sair...')
