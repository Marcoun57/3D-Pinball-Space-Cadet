import pygame
from Balle import Ball  # Importer avec la casse correcte
from Flippers import Flipper

pygame.init()  # Initialisation de Pygame
WIDTH, HEIGHT = 800, 600  # Paramètres de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Initialise l'écran
pygame.display.set_caption("Jeu de Pinball")

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialiser la balle
ball = Ball(WIDTH // 2, HEIGHT // 2, 15, 5, 5, WHITE)

# Initialiser les flippers
flipper_width = 100
flipper_height = 20
flipper_speed = 10
left_flipper = Flipper(WIDTH // 4 - flipper_width // 2, HEIGHT - 30, flipper_width, flipper_height, flipper_speed, WHITE)
right_flipper = Flipper(3 * WIDTH // 4 - flipper_width // 2, HEIGHT - 30, flipper_width, flipper_height, flipper_speed, WHITE)

running = True
clock = pygame.time.Clock()  # Pour contrôler la vitesse de la boucle

while running:  # Boucle principale
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and left_flipper.x > 0:
        left_flipper.move_left()
    if keys[pygame.K_RIGHT] and left_flipper.x + flipper_width < WIDTH // 2:
        left_flipper.move_right()

    if not ball.update(WIDTH, HEIGHT):
        running = False

    screen.fill(BLACK)  # Effacer l'écran

    ball.draw(screen)
    left_flipper.draw(screen)
    right_flipper.draw(screen)

    pygame.display.flip()  # Rafraîchir l'affichage

    clock.tick(60)  # Limiter la boucle à 60 FPS

pygame.quit()