import pygame

class Ball:
    def __init__(self, x, y, radius, speed_x, speed_y, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color

    def update(self, screen_width, screen_height):
        self.x += self.speed_x
        self.y += self.speed_y

        # Vérifier les collisions avec les bords de l'écran
        if self.x - self.radius <= 0 or self.x + self.radius >= screen_width:
            self.speed_x = -self.speed_x  # Rebondir horizontalement
        if self.y - self.radius <= 0:
            self.speed_y = -self.speed_y  # Rebondir verticalement (en haut)
        if self.y + self.radius >= screen_height:
            print("Game Over!")
            return False
        return True

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

pygame.init() # Initialiser Pygame
WIDTH, HEIGHT = 800, 600 # Paramètres de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Initialise l'écran

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paramètres de la balle
ball = Ball(WIDTH // 2, HEIGHT // 2, 15, 5, 5, WHITE)

running = True
while running: # Boucle principale

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    
    # Mettre à jour la position de la balle
    running = ball.update(WIDTH, HEIGHT)
    
    screen.fill(BLACK) # Effacer l'écran
    ball.draw(screen) # Dessiner la balle
    pygame.display.flip()  # Rafraîchir l'affichage

pygame.quit()
