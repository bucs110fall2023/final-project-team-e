import pygame

class Message:
    
    def __init__ (self, display, msg, msg_color, x, y, size):
        font_style = pygame.font.SysFont(None, size)
        mesg = font_style.render(msg, True, msg_color)
        mesg_rect = mesg.get_rect(center=(x, y))
        display.blit(mesg, mesg_rect)