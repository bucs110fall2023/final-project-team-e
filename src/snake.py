import pygame

class Snake:
    
    def __init__(self, display, color, x, y, w, h):
        pygame.draw.rect(display, color, [x, y, w, h])
    
    def snake_body(self, list, display, color, size):
        for x in list:
            pygame.draw.rect(display, color, [x[0], x[1], size, size])
    