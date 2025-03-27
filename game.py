import pygame
from pygame import gfxdraw
import noise 
import numpy as np 

FPS = 24
W,H = 600, 800
R = 200
CC = (230, 64, 213) #pink
RUNNING = True

pygame.init()
screen = pygame.display.set_mode((W,H)) #with height
clock = pygame.time.Clock()
index = 0


#fixes the center issue and provides anti-aliasing  
def draw_circle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color)


while running:
    #background
    screen.fill((255, 255, 255))

    #perlin noice based color switching
    index += 0.1
    y = noise.pnoise1(index)
    print(y)
    if y > 0.5: 
        circle_color = (0, 0, 0)
    else :
        circle_color = (230, 64, 213)

    #draw filled circle with an offset to center it the screen
    #pygame.draw.ellipse(screen, circle_color, ((W/2)-(R/2), (H/2)-(R/2), R, R))

    draw_circle(screen,round(W/2), round(H/2), R, circle_color)


    x, y = pygame.mouse.get_pos()

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse clicked at:", x, y)
            #todo intersect function with circle 
            #log bci activity by timestamping the button press 


    pygame.display.flip() #draw call
    clock.tick(FPS)


pygame.quit()
