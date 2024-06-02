km = float(input("Digite a quantidade de Km: "))
d = float(input("Digite a quantidade de dias: "))

td = 60 * d

tkm = km * 0.15

v = td + tkm

print('O valor a pagar é R$ {:.2f}'.format(v))

