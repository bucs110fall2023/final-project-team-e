import pygame

class Apple:
    
    def __init__(self, x, y, display, color, size):
        pygame.draw.rect(display, color, [x, y, size, size])
        