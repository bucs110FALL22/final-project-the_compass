import pygame
import time
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


clock = pygame.time.Clock()
clock.tick(10)

pygame.init()

is_on = True
width = 600
height = 400

size = [width,height]
#this is the main loop


    



#player sprites due to world size have to be 30x80~ but prolly less due to white space


class Player(pygame.sprite.Sprite):
  def __init__(user):
        super(Player, user).__init__()
        user.pl_surf = pygame.Surface((30,44))
        user.pl_surf.fill((250, 250, 250))
        user.pl_rect = user.pl_surf.get_rect()
    
        user.screen.blit(pl_surf, (width-550, height-100))
        pygame.display.flip()

        user.idles = ["Idle_one.png", "Idle_two.png", "Idle_one.png","Idle_three.png","Idle_four.png"]
        user.idle_ind = 0
        user.image = pygame.idles.load(user.runs[user.idle_ind])
        user.rect = user.image.get_rect()
        
        user.runs = ["Walk_1.PNG", "Walk_2.PNG", "Walk_3.PNG"]    #only four here
        user.runs_ind = 0 
        user.image = pygame.image.load(user.runs[user.runs_ind])
        user.rect = user.image.get_rect()


        user.jumps = ["Jump_1.PNG", "Jump_2.PNG", "Jump_3.PNG"]   #three here?
        user.jumps_ind = 0 
        user.image = pygame.image.load(user.jumps[user.jumps_ind])
        user.rect = user.image.get_rect()


        user.dies = []   #three here
        user.dies_ind = 0 
        user.image = pygame.image.load(user.dies[user.dies_ind])
        user.rect = user.image.get_rect()


       user.ends = []    # two here?
       user.ends_ind = 0 
       user.image = pygame.image.load(user.ends[user.ends_ind])
       user.rect = user.image.get_rect()
       user.health = 3


# updates are for movement, animations and to keep player in bounds
    def update():
      for event in pygame.event.get():
        if event.type == KEYUP:   #this will hold idles
          #if amount of time, start doing this
          user.idle_ind = (user.idle_ind + 1) % len(user.idles) 
          user.image = pygame.image.load(user.idles[user.idle_ind])
          nx_frame = user.image.get_rect()
          nx_frame.x = user.rect.x
          nx_frame.y = user.rect.y
          user.rect = nx_frame
          
        if event.type == KEYDOWN:
          if event.key == K_LEFT:
            user.runs_ind = (user.runs_ind + 1) % len(user.idles) 
            user.image = pygame.image.load(user.idles[user.runs_ind])
            nx_frame = user.image.get_rect()
            nx_frame.x = user.rect.x
            nx_frame.y = user.rect.y
            user.x = user.x + .5
            user.rect = nx_frame
            
  
          if event.key == K_RIGHT:
            user.runs_ind = (user.runs_ind + 1) % len(user.idles) 
            user.image = pygame.image.load(user.idles[user.runs_ind])
            nx_frame = user.image.get_rect()
            nx_frame.x = user.rect.x
            nx_frame.y = user.rect.y
            user.x = user.x - .5
            user.rect = nx_frame
    
          if event.key == K_UP:
            user.jumps_ind = (user.jumps_ind + 1) % len(user.jumps) 
            user.image = pygame.image.load(user.jumps[user.jumps_ind])
            nx_frame = user.image.get_rect()
            nx_frame.x = user.rect.x
            nx_frame.y = user.rect.y
            user.y = user.y + 3
            user.rect = nx_frame
            
  
          if event.key == K_DOWN:
            user.image_index = (user.idle_ind + 1) % len(user.idles) 
            user.image = pygame.image.load(user.idles[user.idle_ind])
            nx_frame = user.image.get_rect()
            nx_frame.x = user.rect.x
            nx_frame.y = user.rect.y
            user.rect = nx_frame









        





# when updating for player movemetn is where i think should be the animations as well, I mean if player move rieght then you move 


while is_on:     #this place is always running 


  for event in pygame.event.get():
    if event.type == KEYDOWN:
      if event.key == K_ESCAPE:
        is_on = False

      elif event.type == QUIT:
        is_on = False

    if event.type


player = Player()
#bases for all the animations



class Background():
    def __init__(br):
     br.surf = pygame.Surface((600,400))
     br.image = ["Backgroundpy.PNG"]

class Floor():
  def __init__(fl):
    fl.surf - pygame.Surface((600,100))
    fl.image = ["Groundfloor.png"]
    
#class Cloud():
  def __init__(cl):
    cl.surf = pygame.Surface((20,30))
    cl.image = []
     def update():
       while True:
        cl.x = cl.x -.4
        time.sleep(5)

#class Spike():
  def __init__(sp):
    sp.surf = pyhame.Surface((20,30))
    sp.image = []


# def update(self):
        #when the update method is called, we will increment the index
        self.index += 1
 
        #if the index is larger than the total images
        if self.index >= len(self.images):
            #we will make the index to 0 again
            self.index = 0
        
        #finally we will update the image that will be displayed
        self.image = self.images[self.index]
