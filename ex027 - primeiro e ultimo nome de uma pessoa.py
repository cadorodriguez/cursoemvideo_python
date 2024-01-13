n = str(input('Qual seu Primeiro nome?'))
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('seu ultim nome é {}'.format(nome[len(nome)-1]))