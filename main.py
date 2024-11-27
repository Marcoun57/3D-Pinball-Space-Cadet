import pygame
import random

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de Pinball")

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Effacer l'écran
    screen.fill(BLACK)
    
    # (Ajoute ici le code pour la balle, les flippers, etc.)

    pygame.display.flip()  # Rafraîchir l'affichage

pygame.quit()