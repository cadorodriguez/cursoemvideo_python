altura = float(input('Qual sua altura?'))
peso = float(input('Qual seu peso?'))
imc = peso / (altura**2)
print('Seu imc é {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está com BAIXO PESO')
elif 18.5 <= imc <= 24.99:
    print('Você esta com peso NORMAL ')
elif 25 <= imc <= 29.99:
    print('Você está com SOBREPESO')
else:
    print('Você está com OBESIDADE')