import pygame
import time
import sys

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
)
import image_test from image_test


class Controller:
  def __init__(self):
    pygame.init()
    width = 600
    height = 400

    size = [width,height]
    self.screen = pygame.display.set_mode(size)
    self.background_images = ("../assets/Press_start.png")
    self.background = pygame.image.load(self.background_images)
    self.background = pygame.transform.scale(self.background, size)

  
  def mainloop(self):
  
    
    pygame.mouse.set_visible(1)
    button1 = pygame.draw.rect(self.screen, 'blue', (75, 200, 100, 40))
    button2 = pygame.draw.rect(self.screen, 'red', (425, 200, 100, 40))
    pygame.display.flip()

    while True:
      bg.blit(bg,(0,0))
      for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                ## if mouse is pressed get position of cursor ##
                  pos = pygame.mouse.get_pos()
                ## check if cursor is on button ##
                  if button1.collidepoint(pos):
                    print("You pressed blue button")
                    blueButton()
                    pygame.time.wait(7000)
                  elif button2.collidepoint(pos):
                    print("You pressed red button")
                    redButton()
          
  def blueButton():
    screen.fill('blue')  #this is start button, change this to level select
    lvl1 = pygame.draw.rect(self.screen, 'blue', (75, 200, 100, 40))
    lvl2 = pygame.draw.rect(self.screen, 'red', (425, 200, 100, 40))
    pygame.display.flip()

    while True:
      bg.blit(bg,(0,0))
      for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                ## if mouse is pressed get position of cursor ##
                  pos = pygame.mouse.get_pos()
                ## check if cursor is on button ##
                  if lvl1.collidepoint(pos):
                    print("You pressed blue button")
                    lvl1()
                    pygame.time.wait(7000)
                  elif lvl2.collidepoint(pos):
                    print("You pressed red button")
                    lvl2()
    quit()

  def redButton():
    screen.fill('red')   #this will be the ingame quit button, clicking this will close out the aplication
    pygame.display.flip()
    time.wait(9)
    pygame.display.quit()
    pygame.quit()
    exit()


 

def lvl1():
  #screen.fill("green")
  Background()
  Floor()
  pygame.display.flip()
  Player()
  Endflag()
    while True:
      if player.pos() >= (.100):
        lvl2()
  #Clouds()
  #Enemy() # I would have to find a way to be able to place down and have them move too 
  Player()
  
  def quit():
    pygame.time.wait(1000)
    main()
  main()

    pygame.display.flip()

Controller()
