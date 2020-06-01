# Refaça o Exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 042 - ANALISANDO TRIÂNGULOS V.2.0'))
print('-' * 100)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        tipo = 'EQUILÁTERO'
    elif r1 != r2 != r3 != r1:
        tipo = 'ESCALENO'
    else:
        tipo = 'ISÓSCELES'
    print(f'Os segmentos acima podem formar um triângulo {tipo}!')
else:
    print('Os segmentos acima NÃO podem formar um triângulo!')

print('-' * 100)

input('Pressione ENTER para sair...')
