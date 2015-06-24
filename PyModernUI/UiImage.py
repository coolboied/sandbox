import pygame
from UiObject import *

class UiImage(UiObject):
    FILLPLAT = 0
    FILLSTRETCHX = 1
    FILLSTRETCHY = 2
    FILLSTRETCHXY = 3

    def __init__(self,x=0,y=0,height=0, weight=0):
        UiObject.__init__(self,x,y,height,weight)

    def set_image(self, fileName,fillType=0):
#TODO fillType
        self.image = pygame.image.load(fileName).convert_alpha()
        self.image = pygame.transform.scale(self.image,(100,100))

    def draw(self, screen):
        screen.blit(self.image, (self.x,self.y))
