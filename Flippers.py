import pygame

# Dimensions de l'écran
WIDTH = 800
HEIGHT = 600

# Paramètres des flippers
flipper_width = 100
flipper_height = 20
flipper_speed = 10

# Positions des flippers
left_flipper_x = WIDTH // 2 - flipper_width - 10
right_flipper_x = WIDTH // 2 + 10
flipper_y = HEIGHT - 40  # Flippers à 40 pixels du bas de l'écran

# Boucle principale
running = True
while running:
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
        right_flipper_x <= ball_x <= right_flipper_x + flipper_width
    ):
        ball_speed_y = -ball_speed_y  # La balle rebondit sur les flippers
    
    # Effacer l'écran
    screen.fill(BLACK)
    
    # Dessiner la balle
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)
    
    # Dessiner les flippers
    pygame.draw.rect(screen, WHITE, (left_flipper_x, flipper_y, flipper_width, flipper_height))
    pygame.draw.rect(screen, WHITE, (right_flipper_x, flipper_y, flipper_width, flipper_height))
    
    pygame.display.flip()  # Rafraîchir l'affichage

pygame.quit()
