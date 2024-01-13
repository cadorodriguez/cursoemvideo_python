from random import choice

a1 = input('Primeiro aluno:')
a2 = input('Segundo aluno:')
a3 = input('Terceiro aluno:')
a4 = input('Quarto Aluno:')
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O escohido para apagar o quadro foi {}: '.format(escolhido))