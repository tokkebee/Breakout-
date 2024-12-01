# this file has Brick class, which inherits from drawables.
#
# the ball should be able to "bounce" off the Bricks, like it does with the walls.
# when the Ball makes contact with a Brick, the Ball should bounce off, the Brick instance disappears, and one point is added to the score.
from drawable import Drawable
import pygame

class Brick(Drawable): #imported just for kill()
    def __init__(self, x=0, y=0, width=0, height=0, color=(0,0,0)):
        super().__init__(x, y)
        self.__width = width
        self.__height = height
        self.__color = color
    
    def draw(self, surface): #brick's visuals
        pygame.draw.rect(surface, self.__color, self.get_rect())

    #getters
    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height
    
    def getColor(self):
        return self.__color
    def setColor(self, color):
        self.__color = color

    #returns where a drawable's border is
    def leftSide(self):
        loc = self.getLoc()
        return loc[0] - self.__width
    def rightSide(self):
        loc = self.getLoc()
        return loc[0] + self.__width
    def topSide(self):
        loc = self.getLoc()
        return loc[1] - self.__height
    def bottomSide(self):
        loc = self.getLoc()
        return loc[1] + self.__height
    
    def get_rect(self): #brick's hitbox
        location = self.getLoc()
        return pygame.Rect(location[0] - self.__width, location[1] - self.__height, 2 * self.__width, 2 * self.__height) 
    
    def kill(self):
        del self