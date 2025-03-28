import pygame
from pygame import gfxdraw
import noise 
import numpy as np
import colorsys

FPS = 24
W,H = 600, 800
R = 200
RUNNING = True

pygame.init()
screen = pygame.display.set_mode((W,H)) #with height
clock = pygame.time.Clock()
color_update_speed = 0.8
angle = 0

#fixes the center issue and provides anti-aliasing  
def draw_circle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color)


def hsv_to_rgb(h, s=1.0, v=1.0):
    """map HSV [0,1] to RGB [0, 255]."""
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return int(r * 255), int(g * 255), int(b * 255)

def angle_to_hsv(angle):
    """map angle [0, 360] to hue [0, 1] range"""
    return angle/360.0

def angle_to_rgb(angle):
    hue = angle_to_hsv(angle)
    return hsv_to_rgb(hue)


while RUNNING:
    #background
    screen.fill((255, 255, 255))
    
    angle += color_update_speed #fps multiplier 
    angle = angle % 360 #limit the domain between 0 and 360

    cc = angle_to_rgb(angle)
    draw_circle(screen,round(W/2), round(H/2), R, cc)


    x, y = pygame.mouse.get_pos()

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse clicked at:", x, y)


    #draw next frame
    pygame.display.flip() 
    clock.tick(FPS)


pygame.quit()
