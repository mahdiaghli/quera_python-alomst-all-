import time

import pygame

from math import pi

pygame.init()

screen = pygame.display.set_mode((300, 300))

white = (255, 255, 255)

screen.fill(white)

size = 1
color = (0, 0, 0)

while True:
    mylist = input().split()

    if mylist[0] == "change" and mylist[1] == "size":
        size = int(mylist[2])

    elif mylist[0] == "change" and mylist[1] == "color":
        color = (int(mylist[2]), int(mylist[3]), int(mylist[4]))

    elif mylist[0] == "draw" and mylist[1] == "line":
        pygame.draw.line(screen, color, (int(mylist[2]), int(mylist[3])), (int(mylist[4]), int(mylist[5])), size)

    elif mylist[0] == "draw" and mylist[1] == "circle":
        pygame.draw.circle(screen, color, (int(mylist[2]), int(mylist[3])), int(mylist[4]), size)

    elif mylist[0] == "draw" and mylist[1] == "polygon":
        seclist = []
        t = ()
        for i in range(2, len(mylist), 2):
            t = int(mylist[i]), int(mylist[i + 1])
            seclist.append(t)
        print(seclist)

        pygame.draw.polygon(screen, color, seclist, size)

    elif mylist[0] == "end" and mylist[1] == "drawing":
        break
    pygame.display.update()

pygame.display.update()

pygame.image.save(screen, 'draw.png')

while True:
    pygame.event.pump()
    break
