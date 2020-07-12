from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
cpu = randint(0, 2)
print('''Sua JOGADA: 
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA''')
jogador = int(input('Digite a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if cpu == 0:
    if  jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('PARABÉNS, VOCÊ VENCEU!')
    elif jogador == 2:
        print('PERDEU')
    else:
        print('Jogada Inválida')
elif cpu == 1:
    if jogador == 0:
        print('PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('PARABÉNS, VOCÊ VENCEU!!')
    else:
        print('Jogada Inválida')
elif cpu == 2:
    if jogador == 0:
        print('PARABÉNS, VOCÊ VENCEU!!')
    elif jogador == 1:
        print('PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada Inválida')
print('Computador jogou {}'.format(itens[cpu]))
print('Jogador jogou {}'.format(itens[jogador]))
