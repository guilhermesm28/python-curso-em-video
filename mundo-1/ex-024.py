# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 024 - VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO'))
print('-' * 100)

cidade = str(input('Em qual cidade você nasceu? ')).strip()
print(f'Sua cidade inicia com Santo? {cidade[:5].upper() == "SANTO"}')

print('-' * 100)

input('Pressione ENTER para sair...')
