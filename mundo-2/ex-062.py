# Melhore o Exercício 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 062 - PROGRESSÃO ARITMÉTICA V.3.0'))
print('-' * 100)

p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

cont = 10
qtd_termos = 0

while cont > 0:
    print(f'{p1} - ', end='')
    p1 += r
    cont -= 1
    qtd_termos += 1
    if cont == 0:
        cont = int(input('Quantos termos você quer mostrar a mais? '))

print(f'\nProgressão finalizada com {qtd_termos} termos mostrados!')

print('-' * 100)

input('Pressione ENTER para sair...')
