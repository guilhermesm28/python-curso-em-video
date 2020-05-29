# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raíz quadrada.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 006 - DOBRO, TRIPLO E RAÍZ QUADRADA'))
print('-' * 100)

n = int(input('Digite um número: '))

print(f'Dobro de {n}: {n*2}')
print(f'Triplo de {n}: {n*3}')
print(f'Raíz quadrada de {n}: {pow(n,(1/2)):.2f}')

print('-' * 100)

input('Pressione ENTER para sair...')
