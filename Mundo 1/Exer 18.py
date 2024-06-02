from math import sin,cos,tan,radians

a = int(input("Digite o ângulo: "))

s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O seno é {:.2f} e o cosseno é {:.2f} a tangente é {:.2f}' .format(s,c,t))