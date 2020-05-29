# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 011 - PINTANDO PAREDE'))
print('-' * 100)

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura

tinta = area / 2

print(
    f'Sua parede tem a dimensão de {largura} x {altura} e sua área é de {area}m²')
print(f'Para pintar essa parede, você precisara de {tinta} litros de tinta.')

print('-' * 100)

input('Pressione ENTER para sair...')
