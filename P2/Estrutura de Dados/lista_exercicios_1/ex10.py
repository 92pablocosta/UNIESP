# Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador. O
# programa deve solicitar a escolha do usuário e, em seguida, escolher aleatoriamente a escolha do
# computador e determinar o vencedor.

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
#print('O computador escolheu {}'.format(itens[computador]))
print('''Suas opções:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 20)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' * 20)
sleep(1)

if computador == 0:
    if jogador == 0:
        print('Empate')    
    elif jogador == 1:
        print('Jogador PERDE')
    elif jogador == 2:
        print('Jogador VENCE')
    else:
        print('Jogada INVÁLIDA')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')    
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')    
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada INVÁLIDA')
