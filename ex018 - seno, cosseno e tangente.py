import math
a = float(input('Digite o ângulo:'))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('O ângulo de {} tem o Seno de {:.2f}'.format(a, sen))
print('O ângulo de {} tem o Coseno de {:.2f}' .format(a, cos))
print('O ângulp de {} tem a Tangente de {:.2f}' .format(a, tan))