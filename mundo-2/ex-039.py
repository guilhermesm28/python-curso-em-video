# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. 
# BÔNUS: Verificar sexo e singular/plural

from datetime import date

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 039 - ALISTAMENTO MILITAR'))
print('-' * 100)

sexo = str(input('Digite seu sexo: ')).strip().upper()
nascimento = int(input('Ano de nascimento: '))
hoje = date.today().year
idade = hoje - nascimento

if idade >= 1:
    if idade == 1:
        sp_a = 'ano'
    else:
        sp_a = 'anos'
    print(f'\nQuem nasceu em {nascimento} completa {idade} {sp_a} em {hoje}.')
    if sexo[:1] == 'M':
        if idade > 18:
            maior = idade - 18
            print(f'Você já deveria ter se alistado há {maior} {sp_a}.\nSeu alistamento seria em {hoje - maior}.')
        elif idade < 18:
            menor = 18 - idade
            if menor == 1:
                sp_a = 'ano'
                sp_f = 'falta'
            else:
                sp_a = 'anos'
                sp_f = 'faltam'
            print(f'Ainda {sp_f} {menor} {sp_a} para o alistamento.\nSeu alistamento será em {hoje + menor}.')
        else:
            print(f'Você precisa se alistar IMEDIATAMENTE!')
    else:
        print('Você não precisa se alistar. O alistamento é obrigatório apenas para os homens')
elif idade == 0:
    print('Acabou de nascer mano, vai demorar pra se alistar (18 anos ainda)!')
else:
    print('Você nem nasceu ainda, mano!')

print('-' * 100)

input('Pressione ENTER para sair...')
