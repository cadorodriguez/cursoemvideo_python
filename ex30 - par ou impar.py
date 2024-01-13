numero=int(input('Digite um número inteiro para verificar se é par ou impar:'))
verificar = numero%2
if verificar == 0:
    print('número {} é PAR'.format(numero))
else:
    print('número {} é impar'.format(numero))