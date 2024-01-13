dias = int(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos KM foi rodado?'))
valor = (dias*60) + (km*0.15)
print('O valor do aluguel é: R${:.2f}'.format(valor))