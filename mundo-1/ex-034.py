# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 034 - AUMENTOS MÚLTIPLOS'))
print('-' * 100)

salario = float(input('Digite seu salário: R$ '))

if salario > 1250:
    aumento = salario * 1.10
else:
    aumento = salario * 1.15

print(f'Seu novo salário é R$ {aumento:.2f}')

print('-' * 100)

input('Pressione ENTER para sair...')
