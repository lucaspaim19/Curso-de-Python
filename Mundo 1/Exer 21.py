import pygame

# Inicializa o mixer do Pygame
pygame.mixer.init()

# Carrega o arquivo de música
pygame.mixer.music.load('C:/Users/Lucas/Downloads/mc_saci.mp3')

# Toca a música
pygame.mixer.music.play()

# Mantém o programa rodando até que a música termine
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
