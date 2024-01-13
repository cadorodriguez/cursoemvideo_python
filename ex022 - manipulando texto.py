nome = str(input('Digite seu nome completo:')).strip()
'''strip serve para tirar espaços no inicio e fim do texto'''
print('Analisando seu nome:')
print('Seu nome em caixa alta é: {}'.format(nome.upper()))
print('Seu nome me caixa baixa é: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
