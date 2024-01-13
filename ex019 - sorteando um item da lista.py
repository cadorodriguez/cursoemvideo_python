import random
from random import shuffle

a1 = input('Nome do Primeiro aluno:')
a2 = input('Nome do Segundo aluno:')
a3 = input('Nome do Terceiro aluno:')
a4 = input('Nome do Quarto aluno:')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação é:')
print(lista)