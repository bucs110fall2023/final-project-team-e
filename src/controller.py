import pygame
import time
import random
from .snake import Snake
from .apple import Apple

class Controller:
  
  def __init__(self):
    self.width = 800
    self.height = 600
    self.display = pygame.display.set_mode((self.width,self.height))
    pygame.display.update()
    pygame.display.set_caption("CS 110 Final Project")
    self.color_snake = "blue" #temporary color choices
    self.color_apple = "red"
    self.clock = pygame.time.Clock()
    self.game_over_choice = False
    
  def mainloop(self):
    
    self.gameloop()

  #def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
    
    snake_speed = 25
    snake_block = 15
    
    x1 = self.width/2
    y1 = self.height/2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 3
    
    apple_x = random.randrange(snake_block, self.width - snake_block)
    apple_y = random.randrange(snake_block, self.height - snake_block)
    
    game_over = False    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_q:
                    self.game_over_choice = True
                elif event.key == pygame.K_r:
                    self.mainloop()
                    
        x1 += x1_change
        y1 += y1_change
        
        if x1 >= self.width or x1 <= 0:
            game_over = True
            self.gameoverloop()
        elif y1 >= self.height or y1 <= 0:
            game_over = True
            self.gameoverloop()
        else:
            pass
        
        self.display.fill("black")
        apple = Apple(apple_x, apple_y, self.display, self.color_apple, snake_block)
        
        snake = Snake(self.display, self.color_snake, x1, y1, snake_block, snake_block)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) >= Length_of_snake:
            del snake_List[0]
        else:
            pass
                
        for x in snake_List:
            pygame.draw.rect(self.display, self.color_snake, [x[0], x[1], snake_block, snake_block])
        
        pygame.display.update()
        
        snake_box = pygame.Rect(x1, y1, snake_block, snake_block)
        apple_box = pygame.Rect(apple_x, apple_y, snake_block, snake_block)
        collide = pygame.Rect.colliderect(snake_box, apple_box)
        if collide:
            self.display.fill("black")
            apple_x = random.randrange(snake_block, self.width - snake_block)
            apple_y = random.randrange(snake_block, self.height - snake_block)
            Length_of_snake += 1
       
        self.clock.tick(snake_speed)

    pygame.quit()
    quit()
    
  def gameoverloop(self):
    self.display.fill("black")
    font_style = pygame.font.SysFont(None, 50)
    def message (msg, msg_color, x, y):
        mesg = font_style.render(msg, True, msg_color)
        mesg_rect = mesg.get_rect(center=(x, y))
        self.display.blit(mesg, mesg_rect)
    message("Game Over", "red", self.width/2, self.height/2)
    pygame.display.update()
    pygame.time.wait(1000)
    
    pygame.quit()
    quit()
    