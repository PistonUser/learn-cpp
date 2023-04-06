from ast import And
from pickle import FALSE
import pygame
import time

# Intialize the pygame
pygame.init ()

# create the screen
screen = pygame.display.set_mode((1200, 900))

#title and icon
pygame.display.set_caption("Go Nuts!")

icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

#keyboard pressed defining
Wpressed = False
Spressed = False
Apressed = False
Dpressed = False
Spacepressed = False

#player
squrrielx = 100
squrriely = 100
squrrielwidth = 200
squrrielheight = 200
squrrielxchange = 0
squrrielychange = 0

squrriel_left = pygame.image.load("textures/squrriel textures/squrriel_left.png")
squrriel_left1 = pygame.image.load("textures/squrriel textures/squrriel_left1.png")
squrriel_left2 = pygame.image.load("textures/squrriel textures/squrriel_left2.png")
squrriel_right = pygame.image.load("textures/squrriel textures/squrriel_right.png")
squrriel_right1 = pygame.image.load("textures/squrriel textures/squrriel_right1.png")
squrriel_right2 = pygame.image.load("textures/squrriel textures/squrriel_right2.png")

squrriel_left = pygame.transform.scale(squrriel_left, (squrrielheight,squrrielwidth))
squrriel_left1 = pygame.transform.scale(squrriel_left1, (squrrielheight,squrrielwidth))
squrriel_left2 = pygame.transform.scale(squrriel_left2, (squrrielheight,squrrielwidth))
squrriel_right = pygame.transform.scale(squrriel_right, (squrrielheight,squrrielwidth))
squrriel_right1 = pygame.transform.scale(squrriel_right1, (squrrielheight,squrrielwidth))
squrriel_right2 = pygame.transform.scale(squrriel_right2, (squrrielheight,squrrielwidth))

squrrieldirection = squrriel_right



def player(squrrielx, squrriely):
    screen.blit(squrrieldirection, (squrrielx, squrriely))

#acorn
acornx = 400
acorny = 200
acornwidth = 200
acornheight = 200

acorntexture = pygame.image.load("textures/acorn.png")
acorntexture = pygame.transform.scale(acorntexture, (acornheight,acornwidth))

def acorn(acornx, acorny): 
    screen.blit(acorntexture, (acornx, acorny))

#game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Wpressed = True
            if event.key == pygame.K_s:
                Spressed = True
            if event.key == pygame.K_a:
                Apressed = True
            if event.key == pygame.K_d:
                Dpressed = True
            if event.key == pygame.K_SPACE:
                Spacepressed = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                Wpressed = False
            if event.key == pygame.K_s:
                Spressed = False
            if event.key == pygame.K_a:
                Apressed = False
            if event.key == pygame.K_d:
                Dpressed = False
            if event.key == pygame.K_SPACE:
                Spacepressed = False

    screen.fill((0, 120, 170))

    if Dpressed == True:
        squrrielxchange = 1
        squrrieldirection = squrriel_right

    if Apressed == True:
        squrrielxchange = -1
        squrrieldirection = squrriel_left
    
    if Apressed == False and Dpressed == False:
        squrrielxchange = 0

    if Spressed == True:
        squrrielychange = 1

    if Spressed == False:
        squrrielychange = 0

    if Spacepressed == True:
        squrriely
        


    squrriely += squrrielychange
    squrrielx += squrrielxchange
    player(squrrielx, squrriely)

    acorn1 = acorn(200, 100)
    acorn1
    pygame.display.update()