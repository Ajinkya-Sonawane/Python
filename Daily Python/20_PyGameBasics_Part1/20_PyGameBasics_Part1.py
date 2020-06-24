import pygame
pygame.init()

size = width,height = 500,500
color = (0,0,0)
pos = [2,2]
title = "First Py-Game"

window = pygame.display.set_mode(size)
pygame.display.set_caption(title)

ball = pygame.image.load("ball.png")
ballRect = ball.get_rect()
run = True
while run:
    #Reset the pos 
    pos = 0,0
    pygame.time.delay(100)
    print(pygame.event.get())
    #Handle Arrow Key event
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pos = -10,0
    if keys[pygame.K_RIGHT]:
        pos = 10,0
    if keys[pygame.K_UP]:
        pos = 0,-10
    if keys[pygame.K_DOWN]:
        pos = 0,10
    #Break the loop when ESCAPE is pressed
    if keys[pygame.K_ESCAPE]:
        run = False
    #Move the rectangle
    ballRect = ballRect.move(pos)
    window.fill(color)
    window.blit(ball,ballRect)
    pygame.display.flip()

pygame.quit()

