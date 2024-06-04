n = input('Digite seu nome completo: ').strip()
p = n.split()
print('Seu primeiro nome é {}'.format(p[0]))
print('Seu último nome é {}'.format(p[len(p)-1]))