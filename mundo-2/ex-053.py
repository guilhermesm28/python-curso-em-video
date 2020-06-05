# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 053 - DETECTOR DE PALÍNDROMO'))
print('-' * 100)

frase = str(input('Digite uma frase: ')).replace(' ','').upper()

inverso = frase[::-1]

print(f'O inverso de {frase} é {inverso}')

if frase == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

print('-' * 100)

input('Pressione ENTER para sair...')
