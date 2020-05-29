# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 022 - ANALISADOR DE TEXTOS'))
print('-' * 100)

nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()

print(f'Maiúsculas: {nome.upper()}')
print(f'Minúsculas: {nome.lower()}')
print(f'Quantidade de letras: {len(nome) - nome.count(" ")}')
print(f'Quantidade de letras (primeiro nome): {len(separa[0])}')

print('-' * 100)

input('Pressione ENTER para sair...')
