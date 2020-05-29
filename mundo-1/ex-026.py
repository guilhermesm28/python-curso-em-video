# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 026 - PRIMEIRA E ÚLTIMA OCORRÊNCIA DE UMA STRING'))
print('-' * 100)

frase = str(input('Digite uma frase: ')).upper().strip()

print(f'A letra A aparece {frase.count("A")} vezes.')
print(f'A primeira letra A apareceu na posição {frase.find("A") + 1}')
print(f'A última letra A apareceu na posição {frase.rfind("A") + 1}')

print('-' * 100)

input('Pressione ENTER para sair...')
