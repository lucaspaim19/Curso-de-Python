p = float(input("Digite um preço: "))

d = (p*0.05)

pd = p-d

print('Seu produto custava R$ {:.2f} com desconto de 5% = {:.2f} , ficará R$ {:.2f}'.format(p,d,pd))
