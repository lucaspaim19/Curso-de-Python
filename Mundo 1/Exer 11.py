# Solicita ao usuário uma altura
a = float(input("Digite um número: "))

# Solicita ao usuário uma largura
l = float(input("Digite um número: "))

#metros quadrados
m = a*l

#tinta em litros
t = m/2

print('Sua parede tem {} de altura, {} de largura,{} em metros quadrado, sendo assim para pintar será necessário {} litros de tinta'.format(a,l,m,t))

