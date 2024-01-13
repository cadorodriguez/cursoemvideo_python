radar = float(input('A velocidade do carro foi Km'))
if radar > 80:
    print('A velocidade do carro foi de Km {:.0F} \nE para essa infração o valor da multa é R$ {:.2f}'.format(radar,(radar-80)*7))
print('Dirija com Cuidado!')