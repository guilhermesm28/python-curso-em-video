# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 018 - SENO, COSSENO E TANGENTE'))
print('-' * 100)

angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O ângulo de {angulo:.2f} tem o SENO de {seno:.2f}')
print(f'O ângulo de {angulo:.2f} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {angulo:.2f} tem a TANGENTE de {tangente:.2f}')

print('-' * 100)

input('Pressione ENTER para sair...')
