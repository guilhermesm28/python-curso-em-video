# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 031 - CUSTO DA VIAGEM'))
print('-' * 100)

distancia = int(input('Digite a distância da viagem em km: '))

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print(f'O preço da sua passagem será de R$ {preco:.2f}')

print('-' * 100)

input('Pressione ENTER para sair...')
