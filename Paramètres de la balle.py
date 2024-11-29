# Paramètres de la balle
ball_radius = 15
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

# Boucle principale
running = True
while running:
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
    
    # Effacer l'écran
    screen.fill(BLACK)
    
    # Dessiner la balle
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)
    
    pygame.display.flip()  # Rafraîchir l'affichage

pygame.quit()
