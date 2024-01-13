numPrimeiro = float(input('Digite o Primeiro Número: '))
numSegundo = float(input('Digite o Segundo Número: '))
if numPrimeiro > numSegundo:
    print('O Primeiro número {:.0f} é maior que o Segundo número {:.0f}'.format(numPrimeiro, numSegundo))
elif numSegundo > numPrimeiro:
    print('O segundo número {:.0f} é maior que o Primeiro número {:.0f}' .format(numSegundo,numPrimeiro))
elif numPrimeiro == numPrimeiro:
    print('O Primeiro número {:.0f} e o Segundo número {:.0f} são iguais' .format(numPrimeiro,numSegundo))