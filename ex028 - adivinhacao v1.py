from random import randint
from time import sleep

computador = randint(0,5) #faz o computador sortear um número#
print('*-*-' * 20)
print('Vou sortear um número de 0 a 5 e você tenta adivinhar')
print('*-*-' * 20)
jogador = int(input('Digite seu palpite para o número sorteado:'))
print('Aguarde enquanto verificamos.......')
sleep(4)
if jogador == computador:
    print('PARABÉNS!! Você acertou o número')
else:
    print('Você errou! O número sorteado foi {} e não o {}'.format(computador, jogador))

