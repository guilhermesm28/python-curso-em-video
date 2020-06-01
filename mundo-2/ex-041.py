# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 041 - CLASSIFICANDO ATLETAS'))
print('-' * 100)

ano = int(input('Ano de nascimento: '))

hoje = date.today().year
idade = hoje - ano

if idade < 0:
    print('INVÁLIDO! Verifique suas informações...')
else:
    if idade <= 9:
        cat = 'MIRIM'
    elif idade > 9 and idade <= 14:
        cat = 'INFANTIL'
    elif idade > 14 and idade <= 19:
        cat = 'JÚNIOR'
    elif idade > 19 and idade <= 25:
        cat = 'SÊNIOR'
    elif idade > 25:
        cat = 'MASTER'
    print(f'\nIdade: {idade} \nCategoria: {cat}')

print('-' * 100)

input('Pressione ENTER para sair...')
