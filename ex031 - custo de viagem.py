km = int(input('Qual a distancia em KM da viagem?'))
if km <= 200:
    print('Sua viagem de {}km\nVai custar R${:.2f}'.format(km,(km*0.50)))
else:
    print('Sua viagem de {}km\nVai custar R${:.2f}.'.format(km,(km*0.45)))