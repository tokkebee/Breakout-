from drawable import Drawable
import pygame
import random

class Ball(Drawable):
    def __init__(self, x=0, y=0, radius=10, color=(0,0,0)):
        super().__init__(x, y)
        self.__radius = radius
        self.__color = color
        self.__xSpeed = 1
        self.__ySpeed = 1 
    
    def draw(self, surface):
        if self.isVisible():
            pygame.draw.circle(surface, self.__color, self.getLoc(), self.__radius)

    def move(self):
        # Increase __x and __y by some amount
        currentX, currentY = self.getLoc()
        newX = currentX + self.__xSpeed
        newY = currentY + self.__ySpeed 
        self.setX(newX)
        self.setY(newY)

        surface = pygame.display.get_surface()
        width, height = surface.get_size()

        if newX <= self.__radius or newX + self.__radius >= width:
            self.__xSpeed *= -1 

        if newY <= self.__radius or newY + self.__radius >= height:
            self.__ySpeed *= -1 
    
    def get_rect(self):
        location = self.getLoc()
        radius = self.__radius
        return pygame.Rect(location[0] - radius, location[1] - radius, 2 * radius, 2 * radius) 
    
    #returns where a drawable's border is
    def leftSide(self):
        loc = self.getLoc()
        return loc[0] - self.__radius
    def rightSide(self):
        loc = self.getLoc()
        return loc[0] + self.__radius
    def topSide(self):
        loc = self.getLoc()
        return loc[1] - self.__radius
    def bottomSide(self):
        loc = self.getLoc()
        return loc[1] + self.__radius
    
    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def isTouchingBall(self, other):
        pass

    def setXSpeed(self, speed):
        self.__xSpeed = speed

    def getXSpeed(self):
        return self.__xSpeed

    def setYSpeed(self, speed):
        self.__ySpeed = speed

    def getYSpeed(self): 
        return self.__ySpeed