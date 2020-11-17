# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:49:12 2020

@author: 66IN
"""


import pygame,random, sys #pygame is an inbuilt library for python , sys is module to access some functionality 


def ball_animation():
    global ball_speed_x,ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y 
    
    #to bounce the ball on the screen edge
    if ball.top <= 0 or ball.bottom >= screen_height:  #vertical or y axis
        ball_speed_y *= -1
    
    if ball.left <= 0 or ball.right >= screen_width:  #horizontal or x axis 
        ball_restart()
    
    
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def player_animation():
     player.y = player_speed
     if player.top <=0:
         player.top = 0
     if player.bottom >= screen_height:
         player.bottom = screen_height    



def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
     
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed  
    if opponent.top <=0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height  
    


def ball_restart():
    global ball_speed_x,ball_speed_y 
    ball.center = (screen_width/2,screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))


pygame.init() #general setup , initiate pygame 
clock = pygame.time.Clock()


#setting up window 
screen_width = 1280
screen_height = 960
#display surface object , store in screen variable
screen = pygame.display.set_mode((screen_width,screen_height)) 
pygame.display.set_caption("Pong")#title



# now drawing in pygame
    
#game rectangle 
ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30) #pygame.Rect(x,y,width,height) x,y is at top left(0,0)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,10,140)
opponent = pygame.Rect(10,screen_height/2 - 70,10,140)


#for color

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)  


ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0 
opponent_speed = 7
while True: #just to check the user has closed the exit window or not
    
    #handling event
    for event in pygame.event.get(): #this loop will check all user actions
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() #closes entire game 
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            
            if event.key == pygame.K_UP:
                player_speed -= 7
        
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            
            if event.key == pygame.K_UP:
                player_speed -= 7
        
    ball_animation()
    player_animation()
    opponent_animation()
   
    #visuals
    screen.fill(bg_color)        
    pygame.draw.rect(screen,light_grey,player) #pygame.draw.rect(screen,color,rect)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,light_grey,ball)
    #line to seperate 2 sides
    pygame.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))
    
    
    
    
    
    
    #updating window
    pygame.display.flip() #used to draw things on screen
    clock.tick(60) #sand clock defined in a code it limits how fast loop works , its 60fps
    

    
        