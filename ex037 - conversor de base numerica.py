numero = int(input('Digite um número inteiro para conversão: '))
print('[ 1 ] Converter em Binário')
print('[ 2 ] Converter em Octal')
print('[ 3 ] Converter em Hexadecimal')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O número {} em Binário é {}' .format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O número {} em Octal é {}' .format(numero,oct(numero)[2:]))
elif opcao == 3:
    print('O número {} em Hexadecimal é {}' .format(numero, hex(numero)[2:]))
else:
    print('Opção Inválida')
