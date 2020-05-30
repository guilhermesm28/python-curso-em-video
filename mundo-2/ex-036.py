# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 036 - APROVANDO EMPRÉSTIMO'))
print('-' * 100)

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))

meses = anos * 12
prestacao = casa / meses
porcent_salario = salario * 0.30

print(f'\n{meses} parcelas de R$ {prestacao:.2f}.')

if prestacao > porcent_salario:
    print(f'Empréstimo NEGADO! Sua prestação excede 30% do seu salário ({porcent_salario:.2f}).')
else:
    print(f'Empréstimo CONCEDIDO!')

print('-' * 100)

input('Pressione ENTER para sair...')
