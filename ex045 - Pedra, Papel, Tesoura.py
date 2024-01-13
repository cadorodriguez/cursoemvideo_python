from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0, 2)
print('Suas Opções:\n'
'[ 0 ] Pedra\n'
'[ 1 ] Papel\n'
'[ 2 ] Tesoura\n')
jogador = int(input('Qual Sua Jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔÔÔ!!!')
print('-='*20)
print('O Computador escolheu {}.'.format(itens[computador]))
print('Sua escolha foi {}'.format(itens[jogador]))
print('-='*20)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Jogador VENCEU!!')
    elif jogador == 2:
        print('Computador VENCEU!!')
    else:
        print('Opção INVÁLIDA')

elif computador == 1:
    if jogador == 0:
        print('Computador VENCEU!!')
    elif jogador == 1:
        print('EMPATE!!')
    elif jogador == 2:
        print('Jogador VENCEU!!')
    else:
        print('Opção INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('Jogador VENCEU!!')
    elif jogador == 1:
        print('Computador VENCEU!!')
    elif jogador == 2:
        print('EMPATE!!')
    else:
        print('Opção INVÁLIDA')
#else:
    #print('ESCOLHA ENTRE AS OPÇÔES FORNECIDAS')