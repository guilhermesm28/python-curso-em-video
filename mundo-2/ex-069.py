# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 069 - ANÁLISE DE DADOS DO GRUPO'))
print('-' * 100)

h = mulher = maior = 0

while True:
    idade = int(input('Idade: '))
       
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\nContinuar? [S/N] ')).strip().upper()[0]

    if idade >= 18:
        maior += 1
    
    if sexo == 'M':
        h += 1

    if sexo == 'F' and idade < 20:
        mulher += 1

    if continuar == 'N':
        break

print(f'Maiores de 18: {maior}')
print(f'Homens cadastrados: {h}')
print(f'Mulheres com menos de 20 anos: {mulher}')
    
print('-' * 100)

input('Pressione ENTER para sair...')
