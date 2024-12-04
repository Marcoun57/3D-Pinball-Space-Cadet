import pygame

class Flipper:
    def __init__(self, x, y, width, height, speed, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

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
flipper_y = HEIGHT - 30

left_flipper = Flipper(WIDTH // 4 - flipper_width // 2, flipper_y, flipper_width, flipper_height, flipper_speed, (0, 255, 0))
right_flipper = Flipper(3 * WIDTH // 4 - flipper_width // 2, flipper_y, flipper_width, flipper_height, flipper_speed, (0, 255, 0))

running = True
while running: # Boucle principale

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    
    # Contrôles des flippers
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and left_flipper.x > 0:
        left_flipper.move_left()  # Déplacer à gauche

    if keys[pygame.K_RIGHT] and left_flipper.x + flipper_width < WIDTH // 2:
        left_flipper.move_right()  # Déplacer à droite
    
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
        left_flipper.x <= ball_x <= left_flipper.x + flipper_width or
        right_flipper.x <= ball_x <= right_flipper.x + flipper_width):
        ball_speed_y = -ball_speed_y

    # Dessiner les éléments
    screen.fill((0, 0, 0))  # Effacer l'écran
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)
    left_flipper.draw(screen)
    right_flipper.draw(screen)
    pygame.display.flip()  # Mettre à jour l'affichage

pygame.quit()
