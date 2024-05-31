# Solicita ao usuário um valor
v = float(input("Digite um valor:R$ "))

d = v / 3.27

print('Você consegue comprar com esse valor de R$ {} a quantidade de U${:.2f} dólares'.format(v,d))