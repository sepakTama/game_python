"""draw_image1.py"""

import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    """main routine"""
    logo = pygame.image.load("pythonlogo.jpg")

    while True:
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()

        SURFACE.fill((225,225,225))

        SURFACE.blit(logo,(20,50),Rect(50,50,100,100))

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()
