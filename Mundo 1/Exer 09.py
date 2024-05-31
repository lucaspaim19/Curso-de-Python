

# Solicita ao usuário um número
numero = int(input("Digite um número: "))

# Exibe a tabuada do número de 0 até 10
print(f"Tabuada do {numero}:")
for i in range(11):
    print(f"{numero} x {i:2} = {numero * i:2}")