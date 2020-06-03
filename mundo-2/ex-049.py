# Refaça o Exercício 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 049 - TABUADA V.2.0'))
print('-' * 100)

n = int(input('Digite um número para ver sua tabuada: '))

for i in range(1,11):
    print(f'{n} x {i:2} = {n * i:2}')

print('-' * 100)

input('Pressione ENTER para sair...')
