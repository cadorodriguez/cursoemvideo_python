from math import hypot
co = float(input('comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adjacente:'))
hi = hypot(co, ca)
print('A hipotenusa mede {:.2f}' .format(hi))