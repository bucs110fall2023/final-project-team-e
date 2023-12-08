import pygame
import time
import random
from .snake import Snake
from .apple import Apple
from .message import Message

class Controller:
  
  def __init__(self):
    self.width = 800
    self.height = 600
    self.display = pygame.display.set_mode((self.width,self.height))
    pygame.display.update()
    pygame.display.set_caption("CS 110 Final Project")
    self.color_snake = "white" # default color
    self.color_apple = "red"
    self.clock = pygame.time.Clock()
    self.game_over_choice = False
    self.start_screen_choice = True
    
  def mainloop(self):
    '''
    acts as the main function for the game, using other functions to begin the program
    args: none
    return: none
    '''
    self.startscreenloop()
    self.gameloop()

  def startscreenloop(self):
    '''
    creates the start screen for the game, providing the ability to choose either options or to start the game
    args: none
    return: none
    '''
    start_screen = True
    self.display.fill("black")
    options_box = pygame.Rect(18, 15, 75, 25)
    Message(self.display, "Options", "white", 50, 30, 25)
    Message(self.display, "Press Enter to start", "white", self.width/2, self.height/2, 40)
    Message(self.display, "SNAKE GAME", "white", self.width/2, self.height/3, 80)      
    pygame.display.update()
    while start_screen:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start_screen = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if options_box.collidepoint(mouse_position):
                self.options_loop()
                start_screen = False

  def options_loop(self):
    '''
    creates the options screen with choices for color
    args: none
    return: none
    '''
    hitboxes = {
        "red": pygame.Rect(250, 100, 50, 50),
        "blue": pygame.Rect(375, 175, 50, 50),
        "green": pygame.Rect(250, 175, 50, 50),
        "purple": pygame.Rect(500, 175, 50, 50),
        "yellow": pygame.Rect(500, 100, 50, 50),
        "orange": pygame.Rect(375, 100, 50, 50),
        "apple": pygame.Rect(250, 400, 70, 50),
        "orange_fruit": pygame.Rect(375, 400, 70, 50),
        "blueberry": pygame.Rect(500, 400, 70, 50)
    }

    self.display.fill("black")

    pygame.draw.rect(self.display, "red", hitboxes["red"])
    pygame.draw.rect(self.display, "blue", hitboxes["blue"])
    pygame.draw.rect(self.display, "green", hitboxes["green"])
    pygame.draw.rect(self.display, "purple", hitboxes["purple"])
    pygame.draw.rect(self.display, "yellow", hitboxes["yellow"])
    pygame.draw.rect(self.display, "orange", hitboxes["orange"])
    
    Message(self.display, "Apple", "red", 265, self.height - 175, 35)
    Message(self.display, "Orange", "orange", self.width/2, self.height - 175, 35)
    Message(self.display, "Blueberry", "blue", 535, self.height - 175, 35)
    
    Message(self.display, "Choose the color of your snake", self.color_snake, self.width/2, self.height - 550, 40)
    Message(self.display, "Choose the type of fruit", self.color_apple, self.width/2, self.height - 250, 40)
    Message(self.display, "Press any key to return to start menu", "white", self.width/2, self.height - 50, 40)
    
    pygame.display.update()
    
    options_screen = True
    while options_screen:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()
        if event.type == pygame.KEYDOWN:
          self.mainloop()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if hitboxes["red"].collidepoint(mouse_position):
                self.color_snake = "red"
            if hitboxes["orange"].collidepoint(mouse_position):
                self.color_snake = "orange"
            if hitboxes["yellow"].collidepoint(mouse_position):
                self.color_snake = "yellow"
            if hitboxes["green"].collidepoint(mouse_position):
                self.color_snake = "green"
            if hitboxes["blue"].collidepoint(mouse_position):
                self.color_snake = "blue"
            if hitboxes["purple"].collidepoint(mouse_position):
                self.color_snake = "purple"
            if hitboxes["orange_fruit"].collidepoint(mouse_position):
                self.color_apple = "orange"
            if hitboxes["apple"].collidepoint(mouse_position):
                self.color_apple = "red"
            if hitboxes["blueberry"].collidepoint(mouse_position):
                self.color_apple = "blue"

  def gameloop(self):
    '''
    holds the content for once the game begins
    args: none
    return: none
    '''
    snake_speed = 8
    snake_block = 15
    
    x1 = self.width/2
    y1 = self.height/2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 3
    points = 0
    
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
        
        Message(self.display, "Points: " + str(points), "white", 80, 40, 40)

        pygame.display.update()
        
        snake_box = pygame.Rect(x1, y1, snake_block, snake_block)
        apple_box = pygame.Rect(apple_x, apple_y, snake_block, snake_block)
        collide = pygame.Rect.colliderect(snake_box, apple_box)
        if collide:
            self.display.fill("black")
            apple_x = random.randrange(snake_block, self.width - snake_block)
            apple_y = random.randrange(snake_block, self.height - snake_block)
            Length_of_snake += 1
            points += 1
            snake_speed += 2
       
        self.clock.tick(snake_speed)

    pygame.quit()
    quit()
    
  def gameoverloop(self):
    '''
    creates the game over screen with option to restart
    args: none
    return: none
    '''
    game_over_screen = True
    while game_over_screen:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.mainloop()
                game_over_screen = False
      self.display.fill("black")
      Message(self.display, "GAME OVER", "red", self.width/2, self.height/3, 100)
      Message(self.display, "Press Enter to Restart", "red", self.width/2, self.height/2, 40)
      pygame.display.update()
