# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 037 - CONVERSOR DE BASES NUMÉRICAS'))
print('-' * 100)

n = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases abaixo para conversão: 
 [ 1 ] Converter para BINÁRIO
 [ 2 ] Converter para OCTAL
 [ 3 ] Converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'\n{n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif opcao == 2:
    print(f'\n{n} convertido para OCTAL é igual a {oct(n)[2:]}')
elif opcao == 3:
    print(f'\n{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}')
else:
    print('Opção inválida! :(')

print('-' * 100)

input('Pressione ENTER para sair...')
