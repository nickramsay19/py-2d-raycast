import pygame
import structure
import math
from myutils import utils

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('2d Raycasting - Nicholas Ramsay')

# configuration
degrees = 10 # how dense the lines of sight are, higher = slower performance

# define some structures
structs = [
    structure.RectangleStructure(300, 250, 50, 50),
    structure.CircleStructure(100, 100, 20),
    structure.RectangleStructure(50, 400, 400, 25),
]

borders = []
for s in structs:
    for border in s.get_border():
        borders.append(border)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    # handle structures
    for s in structs:
        # draw structures
        if type(s) == structure.RectangleStructure:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(s.x, s.y, s.w, s.h), 1)
        elif type(s) == structure.CircleStructure:
            pygame.draw.circle(screen, (255, 255, 255), (s.x, s.y), s.r, 1)
        elif type(s) == structure.LineStructure:
            pygame.draw.line(screen, (255, 255, 255), (s.x1, s.y1), (s.x2, s.y2), 1)

    # get mouse position
    mouse = pygame.mouse.get_pos()

    # generate light beems
    for theta in range(0, degrees):
        # generate lines of unit length
        for h in range(782): # maximum length before screen border reached
            
            x1 = mouse[0]
            y1 = mouse[1]

            x2 = round(x1 + h * math.sin(math.radians((degrees/360)*theta)))
            y2 = round(y1 + h * math.cos(math.radians((degrees/360)*theta)))

            if (x2,y2) in borders:
                break
            else:
                c = ((782 - h)/782) * 200
                pygame.draw.line(screen, (c,c,c), (x1, y1), (x2,y2), 1)


    # update screen
    pygame.display.flip()
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,0,600,500))
    