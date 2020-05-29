# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# Para esse exercício é preciso instalar o módulo PyGame e também ter um arquivo ex_021.mp3 no mesmo diretório dos exercícios.

from pygame import mixer

print('-' * 100)
print('{: ^100}'.format('EXERCÍCIO 021 - TOCANDO UM MP3'))
print('-' * 100)

mixer.init()

mixer.music.load('ex_021.mp3')

mixer.music.play()

print('-' * 100)

input('Pressione ENTER para sair...')
