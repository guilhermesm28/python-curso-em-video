# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre a mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 029 - RADAR ELETRÔNICO'))
print('-' * 100)

velocidade = int(input('Você está andando a quantos km/h? '))

multa = (velocidade - 80) * 7

if velocidade > 80:
    print('MULTADO!!! O limite da via é 80km/h...')
    print(f'Você deve pagar uma multa de R$ {multa:.2f}!')

print('\nDirija com segurança!')

print('-' * 100)

input('Pressione ENTER para sair...')
