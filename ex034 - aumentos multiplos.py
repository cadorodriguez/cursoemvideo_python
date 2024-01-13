salario = float(input('Qual seu salário atual?'))
minimo = 1320
if salario > minimo:
    print('Com o aumento seu salário de R$ {:.2f} passa a ser de R$ {:.2f}'.format(salario,(salario*0.10)+salario))
else:
    print('Com o aumento seu salário de R$ {:.2f} será de R$ {:.2f}'.format(salario,(salario*0.15)+salario))