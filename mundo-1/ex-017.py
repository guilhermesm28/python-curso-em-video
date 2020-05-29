# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 017 - CATETOS E HIPOTENUSA'))
print('-' * 100)

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
hi = hypot(co, ca)

print(f'A hipotenusa vai medir {hi:.2f}')

print('-' * 100)

input('Pressione ENTER para sair...')
