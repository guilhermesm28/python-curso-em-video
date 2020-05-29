# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 033 - MAIOR E MENOR VALORES'))
print('-' * 100)

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))

menor = v1 # Estamos reduzindo um if ao utilizar essa variável
maior = v1 

# Verificando o menor
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3

# Verificando o maior
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3

print(f'O menor valor digitado foi: {menor}')
print(f'O maior valor digitado foi: {maior}')

print('-' * 100)

input('Pressione ENTER para sair...')
