larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
print('Sua parede tem a dimensão de {:.2f}X{:.2f} e sua área é de {:.3f}m²'.format(larg,alt,(larg*alt)))
print('Para pintar sua parede, você precisará de {}l de tinta'.format((larg*alt)/2))