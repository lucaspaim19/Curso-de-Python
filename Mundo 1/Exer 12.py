p = float(input("Digite um preço: R$ "))

vc = float(input("Digite o valor de desconto: "))

pv = vc/100

d = (p*pv)

pd = p-d

print('Seu produto custava R$ {:.2f} com desconto de {}% = {:.2f} , ficará R$ {:.2f}'.format(p,vc,d,pd))
