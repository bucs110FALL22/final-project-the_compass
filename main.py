import pygame
import controller from controller
#import your controller

def main():
    pygame.init()
    Controller()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()





# because we're making a 2d platformer, we need a title card with start, when you for the first time boot up the game possable little slide show showing why you would be going through the platformer, and tehn the first stage should be a little totorial. Menuing should be there and if you press quit you can leave and see the levels you have completed and have yet to unlock, menue in game should be unpause; restart and quit


# standing left, stading right, walking left, walking right, jumping left, jumping right, crouch left, crouch right, attack left, attack right, crouch walk, 