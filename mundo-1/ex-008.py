# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 008 - CONVERSOR DE MEDIDAS'))
print('-' * 100)

n = float(input('Uma distância em metros: '))

mm = n * 1000
cm = n * 100
dm = n * 10
dam = n / 10
hm = n / 100
km = n / 1000

print(f'{n:.2f} m equivalem a:')
print(f'{mm:.0f} mm')
print(f'{cm:.0f} cm')
print(f'{dm:.0f} dm')
print(f'{dam:.1f} dam')
print(f'{hm:.2f} hm')
print(f'{km:.3f} km')

print('-' * 100)

input('Pressione ENTER para sair...')
