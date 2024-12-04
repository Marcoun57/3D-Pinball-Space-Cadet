import pygame

pygame.init() # Initialiser Pygame
WIDTH, HEIGHT = 800, 600 # Paramètres de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Initialise l'écran

# Paramètres de la balle
ball_radius = 15
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

# Paramètres des flippers
flipper_width = 100
flipper_height = 20
flipper_speed = 10
left_flipper_x = WIDTH // 4 - flipper_width // 2
right_flipper_x = 3 * WIDTH // 4 - flipper_width // 2
flipper_y = HEIGHT - 30

running = True
while running: # Boucle principale

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    
    # Contrôles des flippers
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and left_flipper_x > 0:
        left_flipper_x -= flipper_speed  # Déplacer à gauche

    if keys[pygame.K_RIGHT] and left_flipper_x + flipper_width < WIDTH // 2:
        left_flipper_x += flipper_speed  # Déplacer à droite
    
    # Mise à jour de la position de la balle
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # Vérifier les collisions avec les bords de l'écran
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_speed_x = -ball_speed_x
        
    if ball_y - ball_radius <= 0:
        ball_speed_y = -ball_speed_y
    
    if ball_y + ball_radius >= HEIGHT:
        print("Game Over!")
        running = False
    
    # Vérification des collisions avec les flippers
    if (flipper_y - ball_radius <= ball_y <= flipper_y) and (
        left_flipper_x <= ball_x <= left_flipper_x + flipper_width or
        right_flipper_x <= ball_x <= right_flipper_x + flipper_width):
        ball_speed_y = -ball_speed_y

    # Dessiner les éléments
    screen.fill((0, 0, 0))  # Effacer l'écran
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)
    pygame.draw.rect(screen, (0, 255, 0), (left_flipper_x, flipper_y, flipper_width, flipper_height))
    pygame.draw.rect(screen, (0, 255, 0), (right_flipper_x, flipper_y, flipper_width, flipper_height))
    pygame.display.flip()  # Mettre à jour l'affichage

pygame.quit()
