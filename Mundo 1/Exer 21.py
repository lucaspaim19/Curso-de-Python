import pygame

# Inicializa o mixer do Pygame
pygame.mixer.init()

# Carrega o arquivo de música
pygame.mixer.music.load('C:/Users/Lucas/Downloads/mc_saci.mp3')

# Toca a música
pygame.mixer.music.play()

# Solicita ao usuário um número
numero = int(input("Digite um número: "))

# Exibe a tabuada do número de 0 até 10
print(f"Tabuada do {numero}:")
for i in range(11):
    print(f"{numero} x {i} = {numero * i}")

# Mantém o programa rodando até que a música termine
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)