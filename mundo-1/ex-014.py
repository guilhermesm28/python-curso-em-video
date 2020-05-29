# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 014 - CONVERSOR DE TEMPERATURAS'))
print('-' * 100)

c = float(input('Informe a temperatura em ºC: '))
f = ((9 * c) / 5) + 32

print(f'A temperatura de {c:.2f}ºC corresponde a {f:.2f}ºF.')

print('-' * 100)

input('Pressione ENTER para sair...')
