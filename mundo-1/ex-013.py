# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 013 - REAJUSTE SALARIAL'))
print('-' * 100)

salario = float(input('Qual o salário do funcionário? R$ '))
aumento = salario * 15 / 100
novo_salario = salario + aumento

print(
    f'Com o aumento de 15% (R$ {aumento:.2f}), o funcionário que ganhava R$ {salario:.2f} passa a ganhar R$ {novo_salario:.2f}.')

print('-' * 100)

input('Pressione ENTER para sair...')
