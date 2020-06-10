# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 057 - VALIDAÇÃO DE DADOS'))
print('-' * 100)

sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Dados incorretos. Digite novamente seu sexo: [M/F] ')).strip().upper()[0]

if sexo == 'M':
    print('Sexo MASCULINO!')
else:
    print('Sexo FEMININO!')

print('-' * 100)

input('Pressione ENTER para sair...')
