import pygame
import random

pygame.init() # Initialisation de Pygame
WIDTH, HEIGHT = 800, 600 # Paramètres de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Initialise l'écran
pygame.display.set_caption("Jeu de Pinball")

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

running = True
while running: # Boucle principale

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK) # Effacer l'écran
    
    # (Ajoute ici le code pour la balle, les flippers, etc.)

    pygame.display.flip()  # Rafraîchir l'affichage

pygame.quit()