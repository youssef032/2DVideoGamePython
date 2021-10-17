import pygame
import random

#To initalize the game
pygame.init()

#Screen dimensions
screen = pygame.display.set_mode((800, 600))

#Background of game
Background = pygame.image.load('backgroundforgame.png')

#Displays game name and logo
pygame.display.set_caption("Shooting game")
#Logo by Freepik
logo = pygame.image.load('sedan.png')
pygame.display.set_icon(logo)

x = random.randint(0, 720)

#Car
CarImage = pygame.image.load('baby-car.png')
CarX = 400
CarY = 400
CarX_change = 0

#Bullet
BulletImage = pygame.image.load('bullet.png.png')
BulletX = 400
BulletY = 400
BulletX_change = 0
Bullet_state = "ready"

#Enemy
if x>=CarX:
    EnemyImage = pygame.image.load('pterodactyl-dinosaur-bird-shapeleft.png')
    EnemyX = x
    EnemyY = 395
    EnemyX_change = -0.3

elif x<CarX:
    EnemyImage = pygame.image.load('pterodactyl-dinosaur-bird-shaperight.png')
    EnemyX = x
    EnemyY = 395
    EnemyX_change = 0.3

def Car(x, y):
    screen.blit(CarImage, (x, y))
def Enemy(x, y):
    screen.blit(EnemyImage, (x, y))
def bullet(x, y):
    global Bullet_state
    Bullet_state = "fire"
    screen.blit(BulletImage, (x, y))


#How to quit the game
running = True
while running:
    # Background color - Silver
    screen.fill((192, 192, 192))
    screen.blit(Background, (0, 0))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                CarX_change = -0.2
                #print("left")

            if event.key == pygame.K_RIGHT:
                CarX_change = 0.3
               #print("right")

        if event.type== pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                CarX_change = 0
                #print("released")

    #Causes car to move in the x direction
    CarX += CarX_change
    EnemyX +=EnemyX_change

# Prevents car from escaping the screen boundaries
    if CarX <= 0:
        CarX = 0

    elif CarX >= 672:
        CarX = 672

# Prevents enemy from escaping the screen boundaries
    if EnemyX <= 0:
            EnemyX = 0

    elif EnemyX >= 736:
            EnemyX = 736

#Functions to display game characters
    Car(CarX, CarY)
    Enemy(EnemyX, EnemyY)

    pygame.display.update()
