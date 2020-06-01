# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 043 - IMC'))
print('-' * 100)

peso = float(input('Digite seu peso: (kg) '))
altura = float(input('Digite sua altura: (m) '))

imc = peso / altura**2

if imc < 18.5:
    status = 'Abaixo do peso'
elif 18.5 <= imc < 25:
    status = 'Peso ideal'
elif 25 <= imc < 30:
    status = 'Sobrepeso'
elif 30 <= imc < 40:
    status = 'Obesidade'
else:
    status = 'Obesidade Mórbida'

print(f'\nIMC: {imc:.2f} \nStatus: {status}')

print('-' * 100)

input('Pressione ENTER para sair...')
