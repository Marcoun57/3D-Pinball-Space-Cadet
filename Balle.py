import pygame

pygame.init() # Initialiser Pygame
WIDTH, HEIGHT = 800, 600 # Paramètres de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Initialise l'écran

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paramètres de la balle
ball_radius = 15
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

running = True
while running: # Boucle principale

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    
    # Mettre à jour la position de la balle
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # Vérifier les collisions avec les bords de l'écran
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_speed_x = -ball_speed_x  # Rebondir horizontalement

    if ball_y - ball_radius <= 0:
        ball_speed_y = -ball_speed_y  # Rebondir verticalement (en haut)
    
    if ball_y + ball_radius >= HEIGHT:
        print("Game Over!")
        running = False
    
    screen.fill(BLACK) # Effacer l'écran
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius) # Dessiner la balle
    pygame.display.flip()  # Rafraîchir l'affichage

pygame.quit()
