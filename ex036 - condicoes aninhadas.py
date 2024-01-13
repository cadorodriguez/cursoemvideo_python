valorCasa = float(input('Qual o valor da casa R$ ?'))
salario =  float(input('Qual sua renda mensal R$ ?'))
tempoFinanciamento = (int(input('Em quantos meses vai ser o financiamento?'))*12)
prestacao = float(valorCasa/tempoFinanciamento)
corte = ((30/100)*salario)

if prestacao<corte:
    print('\033[1;42m Sua renda mensal renda é compativel com o valor do financiamento\033[m')
    print('Para o valor da casa de R${:.2f} em {:.1f} anos, sua prestação vai ficar em R$ {:.2f}'.format(valorCasa,(tempoFinanciamento/12),prestacao))

elif prestacao>corte:
    print('\033[1;41m Desculpe! Sua renda mensal não é compativel com o valor do financiamnto\033[m')
    print('Para aprovação do financiamente dessa casa no valor R$ {:.2f} sua parcela mensal precisa ser menor que {:.2f}'.format(valorCasa,corte))

else:
    print('Agradecemos o contato')