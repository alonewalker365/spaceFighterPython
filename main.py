import pygame
import time
import random
import math
win = pygame.display.set_mode((800,600))
pygame.display.set_caption('space dodge')



score_value=0

playerimg=pygame.image.load('player.png')
playerx=370
playery=480
pxchange=0
def player(x,y):
    win.blit(playerimg,(x,y))
enemyimg=[]
enemyx=[]
enemyy=[]
exchange=[]


for i in range(3):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0,768))
    enemyy.append(random.randint(40,100))
    exchange.append(0.1)
def enemy(x,y,i):
    win.blit(enemyimg[i],(x,y))


bulimg=pygame.image.load('bullet.png')
bulletx=0
bullety=480
bychange=0.3
state="ready"
def bullet(x,y):
    global state
    state="fire"
    win.blit(bulimg,(x+10,y+5))
def iscollision(enemyx,enemyy,bulletx,bullety):
    d=math.sqrt(math.pow(enemyx-bulletx,2)+math.pow(enemyy-bullety,2))
    if d<27:
        return True
    else:
        return False


run = True
while run:
    win.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pxchange=-0.1
            if event.key == pygame.K_RIGHT:
                pxchange= 0.1
            if event.key == pygame.K_SPACE:
                if state is "ready":

                    bulletx=playerx
                    bullet(bulletx,bullety)
        if event.type == pygame.KEYUP:
            pxchange=0


    playerx+=pxchange
    for i in range(3):
        if playerx <= 0:
            playerx = 0
        if playerx >= 768:
            playerx = 768
        if enemyx[i] <= 0:
            enemyy[i] += 50
            exchange[i] = 0.1
        if enemyx[i] >= 768:
            enemyy[i] += 50
            exchange[i] = -0.1
        enemyx[i] += exchange[i]
        enemy(enemyx[i], enemyy[i], i)
        if enemyy[i]>448:
            run=False


    if bullety<=0:
        bullety=480
        state="ready"

    if state is "fire":
        bullet(bulletx,bullety)
        bullety-=bychange
    for i in range(3):
        collision = iscollision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            bullety = 480
            state = "ready"

            score_value += 1
            if score_value==20:
                run=False
            enemyx[i] = random.randint(0, 768)
            enemyy[i] = random.randint(40, 100)






    player(playerx,playery)


    pygame.display.update()


pygame.quit()
