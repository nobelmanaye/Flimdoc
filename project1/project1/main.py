'''
Nobel Manayhe

Implements an automatcially moving orb that is followed by a camera

'''
import pygame
import os
from vector2D import Vector2
import secrets

# Two different sizes now! Screen size is the amount we show the player,
#  and world size is the size of the interactable world
SCREEN_SIZE = Vector2(1300, 1200)
WORLD_SIZE = Vector2(1200, 1200)



class orb(object):
   '''
   Implements the Orb object
   '''

   def __init__(self,path,velocity,position,offset,negative=False):
      '''
      initializes the Orb oject
      '''

      #initialize variables
      
      self.image= pygame.image.load(path).convert()
      self.velocity = velocity
      #generate starting conditions for the orb(including random desired speeds, velocity & position vecs)
      
      desiredspeed = [x for x in range (80,140,1)] + [-x for x in range(80,140,1)] + [0,0,0,0,0]
      self.velocity.x = 5
      self.velocity.y = 0
      
      if negative:
         self.velocity.x = -5
      self.position = position
      
      self.offset = offset
   
   def getoffset(self):
      '''
      Returns the offset of the orb
      '''
      return self.offset

   def getPosition(self):
      '''
      Returns the positional vector of the orb
      '''
      return self.position
   def getX(self):

      return self.position.x

   def getY(self):
      return self.position.y

   def getWidth(self):
      '''
      Returns the width of the orb image
      '''
      return self.image.get_width()

   def getHeight(self):
      '''
      Returns the height of the orb
      '''
      return self.image.get_height()
   def draw(self):
      '''
       Draws the orb
      '''
      self.image.set_colorkey(self.image.get_at((0,0)))

   def getSize(self):
      '''
      Returns the size of the orb
      '''
      return self.image.get_size()

   
      
   def update(self,position,time):
      '''
      Updates the position of the orb so that it does not fall of the edge
      '''

      #store variables that check for the edge
      oldpos = self.position
      newposy = oldpos.y + self.velocity.y*time.get_time()/1000
      newposx = oldpos.x +self.velocity.x*time.get_time()/1000

      # if is about to cross the screen, reverse the velocity


      #update the position 
      self.position.y = oldpos.y + ((self.velocity.y)*time.get_time()/1000)
      self.position.x = oldpos.x + ((self.velocity.x)*time.get_time()/1000)
      

def getOffset(trackingObject):
   '''
   returns a Vector2 variable containing the offset for drawing things to the screen.
   '''
   return Vector2(max(0,
                        min(trackingObject.position.x + (trackingObject.image.get_width() // 2) - \
                            (SCREEN_SIZE[0] // 2),
                            WORLD_SIZE[0] - SCREEN_SIZE[0])),
                    max(0,
                        min(trackingObject.position.y + (trackingObject.image.get_height()// 2) - \
                            (SCREEN_SIZE[1] // 2),
                            WORLD_SIZE[1] - SCREEN_SIZE[1])))
def main():
   
   # initialize the pygame module
   pygame.init()
   # load and set the logo
   
   pygame.display.set_caption("Camera")
   
   screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

   
   # Let's make a background so we can see if we're moving
   background = pygame.image.load(os.path.join("images", "background.png")).convert()
   
   #intialize necessary vectors,paths for movement of orb and screen
   position = Vector2(-100,400)
   pos2 = Vector2(800,400)
   velocity = Vector2(0,0)
   vel = Vector2(0,0)
   offset = Vector2(0,0)
   path = os.path.join("images", "im1.png")
   path2 =os.path.join("images", "im2.png")
   Orb = orb(path,velocity,position,offset)
   Orb2  =orb(path2,vel,pos2,offset,True)
   Orb.draw()
   Orb2.draw()
     
   #Tick the clock
   gameClock = pygame.time.Clock()
   
   # define a variable to control the main loop
   RUNNING = True

   touched = False
   # main loop
   while RUNNING:

     
      # Draw everything, adjust by offset
      screen.blit(background,(0,0))
      screen.blit(Orb.image, list(Orb.position))
      screen.blit(Orb2.image, list(Orb2.position))
      Orb.update(WORLD_SIZE,gameClock)
      Orb2.update(WORLD_SIZE,gameClock)
      
      
      # Flip the display to the monitor
      pygame.display.flip()
      
      # event handling, gets all event from the eventqueue


      for event in pygame.event.get():
            # only do something if the event is of type QUIT or ESCAPE is pressed

            rand = secrets.SystemRandom().randint(0,1)
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
               # change the value to False, to exit the main loop
               RUNNING = False
               

      # Update time and position
      gameClock.tick(60)
      ticks = gameClock.get_time() / 1000
      Orb.position += Orb.velocity * ticks
      Orb2.position+= Orb2.velocity * ticks

      # calculate offset


      
      
      
      
  
      
   pygame.quit()
   
   
if __name__ == "__main__":
   main()
