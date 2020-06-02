# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 044 - GERENCIADOR DE PAGAMENTOS'))
print('-' * 100)

preco = float(input('Preço total das compras: R$ '))

print('\nFormas de pagamento:\n[ 1 ] À vista - dinheiro/cheque \n[ 2 ] À vista - cartão \n[ 3 ] 2x - cartão \n[ 4 ] mais de 2x - cartão\n')

opcao = int(input('Digite sua opção: '))

parcelas = 0
desconto = 0
juros = 0

if opcao in range(1,5):
    if opcao == 1:
        preco_final = preco - (preco * 0.10)
        desconto = preco * 0.10
    elif opcao == 2:
        preco_final = preco - (preco * 0.05)
        desconto = preco * 0.05
    elif opcao == 3:
        preco_final = preco
        parcelas = preco_final / 2
    elif opcao == 4:
        tot_parcelas = int(input('Quantas parcelas? '))
        if tot_parcelas > 2:
            preco_final = preco * 1.20
            parcelas = preco_final / tot_parcelas
            juros = preco * 0.20
        else:
            preco_final = 0
            print('\nOPÇÃO INVÁLIDA!')
    print(f'\nValor das parcelas: R$ {parcelas:.2f} \nDesconto: R$ {desconto:.2f} \nJuros: R$ {juros:.2f} \nPreço final: R$ {preco_final:.2f}')
else:
    print('Opção inválida! Tente novamente mais tarde...')

print('-' * 100)

input('Pressione ENTER para sair...')
