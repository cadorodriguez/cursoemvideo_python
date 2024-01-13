primeira = float(input('Qual a média da primeira unidade?'))
segunda = float(input('Qual a média da segunda uniade?'))
terceira = float(input('Qual a média da terceira unidade?'))
quarta = float(input('Qual a média da quarta unidade?'))
média = (primeira+segunda+terceira+quarta)/4
if média < 5:
    print('Sua média foi {:.1f}, e você está \033[1;41m REPROVADO\033[m'.format(média))
elif média >= 5 and média <= 6.9:
    print('Sua média foi {:.1f}, e você está \033[1;43m RECUPERAÇÃO \033[m'.format(média))
else:
    print('Sua média foi {:.1f}, e você está \033[1;42m Aprovado \033[m'.format(média))