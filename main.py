import pygame
from src import controller

def main():
    pygame.init()
    ctrl = controller.Controller()
    ctrl.mainloop()

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
