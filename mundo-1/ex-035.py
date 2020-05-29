# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 035 - ANALISANDO TRIÂNGULO V.1.0'))
print('-' * 100)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima NÃO podem formar um triângulo!')

print('-' * 100)

input('Pressione ENTER para sair...')
