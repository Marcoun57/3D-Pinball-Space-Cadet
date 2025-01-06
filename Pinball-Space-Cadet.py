import random, datetime, time, os, sys
import pygame, pymunk, pyautogui
import pymunk.pygame_util
from pygame import mixer
from pymunk import Vec2d

mixer.init()
global score
score = 0
script_name = os.path.basename(__file__)

pygame.init()
screen = pygame.display.set_mode((1920, 1080))

# Charge le son de démarrage
startup_sound = mixer.Sound(r"son\WELCOME.mp3")
startup_sound.play()

# Charge le son du flipper
flipper_sound = mixer.Sound(r"son\FLIPPER.mp3")

# Charge le son de lancement
launch_sound = mixer.Sound(r"son\LAUNCH.mp3")

# Charge le son de sortie de la balle
ball_exit_sound = mixer.Sound(r"son\RETRY.mp3")

# Son de fin de partie
game_over_sound = mixer.Sound(r"son\GAME-OVER.mp3")

# Charge de l'image de la balle
ball_image = pygame.image.load(r"texture\balle.png")
ball_image = pygame.transform.scale(ball_image, (30, 30))  # Ajuste la taille de l'image

# Charge les images des flippers
flipper_image_left = pygame.image.load(r"texture\flipper_g.png")
flipper_image_left = pygame.transform.scale(flipper_image_left, (110, 90))  # Ajuste la taille de l'image

flipper_image_right = pygame.image.load(r"texture\flipper_d.png")
flipper_image_right = pygame.transform.scale(flipper_image_right, (100, 20))  # Ajuste la taille de l'image


clock = pygame.time.Clock()
running = True

### Physique
space = pymunk.Space()
space.gravity = (0.0, 5000.0)
draw_options = pymunk.pygame_util.DrawOptions(screen)

### Balles
balls = []

### Murs
static_lines = [
    pymunk.Segment(space.static_body, (1060,1000), (950,250), 0), # Mur de droite
    pymunk.Segment(space.static_body, (950,250), (915, 175), 0), # Angle droit 1
    pymunk.Segment(space.static_body, (915, 175), (845, 105), 0), # Angle droit 2
    pymunk.Segment(space.static_body, (845, 105), (775, 70), 0), # Angle droit 3
    pymunk.Segment(space.static_body, (775, 70), (690, 55), 0), # Angle droit 4
    
    pymunk.Segment(space.static_body, (690, 55), (610, 55), 0), # Toit

    pymunk.Segment(space.static_body, (610, 55), (525, 75), 0), # Angle gauche 1
    pymunk.Segment(space.static_body, (525, 75), (495, 45), 0), # Angle gauche 2
    pymunk.Segment(space.static_body, (495, 45), (410, 50), 0), # Angle gauche 3
    pymunk.Segment(space.static_body, (410, 50), (380, 90), 0), # Angle gauche 4
    pymunk.Segment(space.static_body, (380, 90), (380, 120), 0), # Angle gauche 5
    pymunk.Segment(space.static_body, (380, 120), (415, 160), 0), # Angle gauche 6

    pymunk.Segment(space.static_body, (415, 160), (350, 260), 0), # Mur gauche 1
    pymunk.Segment(space.static_body, (350, 260), (355, 350), 0), # Mur gauche 2
    pymunk.Segment(space.static_body, (355, 350), (430, 500), 0), # Mur gauche 3
    pymunk.Segment(space.static_body, (430, 500), (420, 640), 0), # Mur gauche 4
    pymunk.Segment(space.static_body, (420, 640), (355, 710), 0), # Mur gauche 5
    pymunk.Segment(space.static_body, (355, 710), (340, 835), 0), # Mur gauche 6
    pymunk.Segment(space.static_body, (340, 835), (530, 980), 0), # Mur gauche 7

    pymunk.Segment(space.static_body, (405, 240), (393, 280), 0), # Mur ile gauche 1
    pymunk.Segment(space.static_body, (393, 280), (400, 320), 0), # Mur ile gauche 2
    pymunk.Segment(space.static_body, (400, 320), (420, 370), 0), # Mur ile gauche 3
    pymunk.Segment(space.static_body, (420, 370), (453, 413), 0), # Mur ile gauche 4
    pymunk.Segment(space.static_body, (453, 413), (525, 370), 0), # Mur ile gauche 5
    pymunk.Segment(space.static_body, (525, 370), (420, 320), 0), # Mur ile gauche 6
    pymunk.Segment(space.static_body, (420, 320), (405, 280), 0), # Mur ile gauche 7
    pymunk.Segment(space.static_body, (405, 280), (412, 240), 0), # Mur ile gauche 8
    pymunk.Segment(space.static_body, (412, 240), (405, 240), 0), # Mur ile gauche 9

    pymunk.Segment(space.static_body, (515, 185), (590, 150), 0), # Mur ile milieu 1
    pymunk.Segment(space.static_body, (590, 150), (590, 120), 0), # Mur ile milieu 2
    pymunk.Segment(space.static_body, (590, 120), (562, 105), 0), # Mur ile milieu 3
    pymunk.Segment(space.static_body, (562, 105), (520, 140), 0), # Mur ile milieu 4
    pymunk.Segment(space.static_body, (520, 140), (515, 185), 0), # Mur ile milieu 5

    pymunk.Segment(space.static_body, (620, 310), (600, 320), 0), # Mur ile droite 1
    pymunk.Segment(space.static_body, (600, 320), (600, 340), 0), # Mur ile droite 2
    pymunk.Segment(space.static_body, (600, 340), (690, 360), 0), # Mur ile droite 3
    pymunk.Segment(space.static_body, (690, 360), (685, 330), 0), # Mur ile droite 4
    pymunk.Segment(space.static_body, (1000, 1000), (910, 270), 0), # Mur de droite 2
    pymunk.Segment(space.static_body, (910, 270), (880, 190), 0), # Mur de droite 3
    pymunk.Segment(space.static_body, (880, 190), (820, 135), 0), # Mur de droite 4
    pymunk.Segment(space.static_body, (820, 135), (760, 105), 0), # Mur de droite 5
    pymunk.Segment(space.static_body, (760, 105), (720, 120), 0), # Mur de droite 6
    pymunk.Segment(space.static_body, (720, 120), (719, 160), 0), # Mur de droite 7
    pymunk.Segment(space.static_body, (719, 160), (750, 180), 0), # Mur de droite 8
    pymunk.Segment(space.static_body, (750, 180), (800, 230), 0), # Mur de droite 9
    pymunk.Segment(space.static_body, (800, 230), (820, 270), 0), # Mur de droite 10
    pymunk.Segment(space.static_body, (820, 270), (780, 360), 0), # Mur de droite 11
    pymunk.Segment(space.static_body, (780, 360), (795, 370), 0), # Mur de droite 12
    pymunk.Segment(space.static_body, (795, 370), (820, 340), 0), # Mur de droite 13
    pymunk.Segment(space.static_body, (820, 340), (880, 370), 0), # Mur de droite 14
    pymunk.Segment(space.static_body, (880, 370), (845, 460), 0), # Mur de droite 15
    pymunk.Segment(space.static_body, (845, 460), (850, 550), 0), # Mur de droite 16
    pymunk.Segment(space.static_body, (850, 550), (905, 585), 0), # Mur de droite 17
    pymunk.Segment(space.static_body, (905, 585), (915, 660), 0), # Mur de droite 18
    pymunk.Segment(space.static_body, (915, 660), (950, 640), 0), # Mur de droite 19
    pymunk.Segment(space.static_body, (920, 730), (934, 864), 0), # Mur de droite 19
    pymunk.Segment(space.static_body, (934, 864), (795, 975), 0), # Mur de droite 20
    pymunk.Segment(space.static_body, (935, 960), (950, 990), 0), # Mur de droite 20
    pymunk.Segment(space.static_body, (950, 990), (995, 990), 0), # Mur de droite 21
    pymunk.Segment(space.static_body, (935, 960), (850, 1030), 0), # Mur de droite 20
    pymunk.Segment(space.static_body, (850, 1030), (853, 1080), 0), # Mur de droite 21

    pymunk.Segment(space.static_body, (1000,1000), (1060,1000), 0) # Sol de la balle

    
]

for line in static_lines:
    line.elasticity = 0.7
    line.group = 1
space.add(*static_lines)

fp = [(20, -20),(-132, 0),(20, 20)]
mass = 30
moment = pymunk.moment_for_poly(mass, fp)

### Flipper droit
r_flipper_body = pymunk.Body(mass, moment)
r_flipper_body.position = 790, 1000
#r_flipper_shape = pymunk.Poly(r_flipper_body, fp)
r_flipper_shape = pymunk.Segment(r_flipper_body, (0, 0), (-76, 60), 10)
r_flipper_shape.visible = False  # Cache la forme de débogage
space.add(r_flipper_body, r_flipper_shape)

r_flipper_joint_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
r_flipper_joint_body.position = r_flipper_body.position
j = pymunk.PinJoint(r_flipper_body, r_flipper_joint_body, (0, 0), (0, 0))

s = pymunk.DampedRotarySpring(r_flipper_body, r_flipper_joint_body, 0.0, 20000000, 900000)
space.add(j, s)

### Flipper gauche
l_flipper_body = pymunk.Body(mass, moment)
l_flipper_body.position = 525, 1000
#l_flipper_shape = pymunk.Poly(l_flipper_body, [(-x, y) for x, y in fp])
l_flipper_shape = pymunk.Segment(l_flipper_body, (0, 0), (76, 60), 10)
l_flipper_shape.visible = False
space.add(l_flipper_body, l_flipper_shape)

l_flipper_joint_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
l_flipper_joint_body.position = l_flipper_body.position
j = pymunk.PinJoint(l_flipper_body, l_flipper_joint_body, (0, 0), (0, 0))
s = pymunk.DampedRotarySpring(l_flipper_body, l_flipper_joint_body, -0.0, 20000000, 900000)
space.add(j, s)

r_flipper_shape.group = l_flipper_shape.group = 1
r_flipper_shape.elasticity = l_flipper_shape.elasticity = 0.4

def draw_flippers(screen, l_flipper_body, r_flipper_body):
    # Flipper gauche
    l_flipper_pos = l_flipper_body.position
    l_flipper_angle = l_flipper_body.angle
    rotated_left_flipper = pygame.transform.rotate(flipper_image_left, -l_flipper_angle * 180 / 3.14159)
    rect_left = rotated_left_flipper.get_rect()
    # Calculer l'offset pour le pivot gauche
    offset_x = rect_left.width * 0.1  # 10% de la largeur
    offset_y = rect_left.height * 0.9  # 90% de la hauteur
    rect_left.bottomleft = (l_flipper_pos.x - offset_x, l_flipper_pos.y + offset_y)
    screen.blit(rotated_left_flipper, rect_left)

    # Flipper droit
    r_flipper_pos = r_flipper_body.position
    r_flipper_angle = r_flipper_body.angle
    rotated_right_flipper = pygame.transform.rotate(flipper_image_right, -r_flipper_angle * 180 / 3.14159)
    rect_right = rotated_right_flipper.get_rect()
    # Calculer l'offset pour le pivot droit
    offset_x = rect_right.width * 0.9  # 90% de la largeur
    offset_y = rect_right.height * 0.9  # 90% de la hauteur
    rect_right.bottomright = (r_flipper_pos.x + offset_x, r_flipper_pos.y + offset_y)
    screen.blit(rotated_right_flipper, rect_right)

### Bumpers (boules)
plist = [(605, 250), (710, 230),(655,310),(445,110)]

body1 = pymunk.Body(body_type=pymunk.Body.KINEMATIC) # Boule de gauche
body1.position = plist[0]
shape21 = pymunk.Circle(body1, 30)
shape21.elasticity = 1.3
shape21.collision_type = 3
shape21.visible = False 
space.add(body1, shape21)

body2 = pymunk.Body(body_type=pymunk.Body.KINEMATIC) # Boule de droite
body2.position = plist[1]
shape22 = pymunk.Circle(body2, 30)
shape22.elasticity = 1.3
shape22.collision_type = 4
shape22.visible = False 
space.add(body2, shape22)

body3 = pymunk.Body(body_type=pymunk.Body.KINEMATIC) # Boule du milieu
body3.position = plist[2]
shape23 = pymunk.Circle(body3, 30)
shape23.elasticity = 1.3
shape23.collision_type = 5
shape23.visible = False 
space.add(body3, shape23)

body4 = pymunk.Body(body_type=pymunk.Body.KINEMATIC) # Boule du en haut a gauche
body4.position = plist[3]
shape24 = pymunk.Circle(body4, 30)
shape24.elasticity = 1.3
shape24.collision_type = 5
shape24.visible = False 
space.add(body4, shape24)

# Triangle
vertices = [(22, -45), (78, 125), (10, 80)]
body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
body.position = (430,770)
shape3 = pymunk.Poly(body, vertices)
shape3.elasticity = 1.4
shape3.collision_type = 6
shape3.visible = False 
space.add(body, shape3)

vertices = [(-20, -40), (-80, 125), (-5, 80)]
body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
body.position = (880,770)
shape4 = pymunk.Poly(body, vertices)
shape4.elasticity = 1.4
shape4.collision_type = 7
shape4.visible = False 
space.add(body, shape4)

# Balle de départ
def addBall():
    global ballbody, shape1
    mass = 2
    radius = 14
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
    ballbody = pymunk.Body(mass, inertia)
    ballbody.position = 1025, 960
    shape1 = pymunk.Circle(ballbody, radius, (0, 0))
    shape1.elasticity = 0.90
    shape1.collision_type = 0
    space.add(ballbody, shape1)
    balls.append(shape1)

def draw_balls(screen, balls):
    for ball in balls:
        x, y = ball.body.position
        screen.blit(ball_image, (x - 15, y - 15))

# Définit la fonction de rappel de collision, sera appelée lorsque la balle touche les pare-chocs
def bounceOnBump1(space, arbiter,dummy):
    global score
    score += 500
    os.system('cls')
    print("SCORE : ",score)
    mixer.music.load(r"son\BOULE.mp3") #boule gauche
    mixer.music.play()
    time.sleep(0.06)
    return True
def bounceOnBump2(space, arbiter,dummy):
    global score
    score += 500
    os.system('cls')
    print("SCORE : ",score)
    mixer.music.load(r"son\BOULE.mp3") #boule droite
    mixer.music.play()
    time.sleep(0.06)
    return True
def bounceOnBump3(space, arbiter,dummy):
    global score
    score += 500
    os.system('cls')
    print("SCORE : ",score)
    mixer.music.load(r"son\BOULE.mp3") #boule du milieu
    mixer.music.play()
    time.sleep(0.06)
    return True
def bounceOnBump4(space, arbiter,dummy):
    global score
    score += 500
    os.system('cls')
    print("SCORE : ",score)
    mixer.music.load(r"son\TRIANGLE.mp3") #triangle gauche
    mixer.music.play()
    time.sleep(0.06)
    return True
def bounceOnBump5(space, arbiter,dummy):
    global score
    score += 500
    os.system('cls')
    print("SCORE : ",score)
    print("SCORE : ",score)
    mixer.music.load(r"son\TRIANGLE.mp3") #triangle droite
    mixer.music.play()
    time.sleep(0.06)
    return True
def SepCol1(space,arbiter,dummy):
    shape21.color = (31, 163, 5, 255)
def SepCol2(space,arbiter,dummy):
    shape22.color = (31, 163, 5, 255)
def SepCol3(space,arbiter,dummy):
    shape23.color = (31, 163, 5, 255)
def SepCol4(space,arbiter,dummy):
    shape3.color = (191, 48, 48, 255)
def SepCol5(space,arbiter,dummy):
    shape4.color = (191, 48, 48, 255)

# Configurer la fonction de rappel de collision
h1 = space.add_collision_handler(0, 3)
h1.begin = bounceOnBump1
h1.separate = SepCol1
h2 = space.add_collision_handler(0, 4)
h2.begin = bounceOnBump2
h2.separate = SepCol2
h3 = space.add_collision_handler(0, 5)
h3.begin = bounceOnBump3
h3.separate = SepCol3
h4 = space.add_collision_handler(0, 6)
h4.begin = bounceOnBump4
h4.separate = SepCol4
h5 = space.add_collision_handler(0, 7)
h5.begin = bounceOnBump5
h5.separate = SepCol5
#h.separate = changeColor# Listening for key press events

start_time = pygame.time.get_ticks()
ball_spawned = False # Ne démarre pas au lancement du jeu
rounds = 3
pygame.font.init()

while running:
    BG = pygame.image.load("bg.png")
    screen.blit(BG, (0, 0))
    my_font = pygame.font.SysFont('Comic Sans MS', 50)
    text_surface = my_font.render((str(score)), True, (0, 0, 255))
    screen.blit(text_surface, (1620,507))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            timestamp = str(datetime.datetime.now()).replace(' ','_').replace(':','')
            pygame.image.save(screen, f"flipper{timestamp}.png")

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            r_flipper_body.apply_impulse_at_local_point(Vec2d.unit() * -40000, (-100, 0))
            flipper_sound.play()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            l_flipper_body.apply_impulse_at_local_point(Vec2d.unit() * 40000, (-100, 0))
            flipper_sound.play()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Vérifie la balle est sr un ressort
            if ballbody.position.x > 940 and ballbody.position.y < 1060:
                ballbody.apply_impulse_at_local_point(Vec2d.unit() * -6700, (0, 0))
                launch_sound.play()

        # vérifie si 6 secondes se sont écoulées depuis le début du jeu
    if not ball_spawned and pygame.time.get_ticks() - start_time > 6000:
        addBall()
        ball_spawned = True


    ### Dessine les choses
    space.debug_draw(draw_options)

    r_flipper_body.position = 790, 1000
    l_flipper_body.position = 525, 1000
    r_flipper_body.velocity = l_flipper_body.velocity = 3, 3

    space.debug_draw(draw_options)
    draw_balls(screen, balls)
    draw_flippers(screen, l_flipper_body, r_flipper_body)  # Ajoute la ligne

    ### Enlève les boules dehors
    to_remove = []
    for ball in balls:
        if ball.body.position.get_distance((300, 300)) > 1000:
            to_remove.append(ball)
            ball_exit_sound.play() 
            # GameOver après 3 parties
            rounds -= 1
            if rounds <= 0 :
                game_over_sound.play() 
                print('GAME OVER')
                rounds = 0
                res = pyautogui.confirm(text='Restart Game ?', title='Game Over', buttons=['Yes', 'No'])
                if res == "Yes" :
                    exec(f'import {script_name}') # Executer à nouveau le script
            else:
                addBall()
                print('Rounds remaining : ',rounds)

    for ball in to_remove:
        space.remove(ball.body, ball)
        balls.remove(ball)

    ### Mettre à jour la phyisque
    dt = 1.0 / 60.0 / 5.0
    for x in range(5):
        space.step(dt)

    ### Fenêtre du jeu
    pygame.display.flip()
    clock.tick(50)
    pygame.display.set_caption("3D Pinball Space Cadet  |  FPS: " + str(clock.get_fps())[0:4])
