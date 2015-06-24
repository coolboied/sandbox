import pygame
from UiArea import *
class UiObject(UiArea):
    def __init__(self, x=0,y=0,height=0,weight=0):
        UiArea.__init__(self,x,y,height,weight)
        self.surface = pygame.Surface((height,weight))
        self.surface=pygame.Surface.convert_alpha(self.surface)
        self.color = (0,0,0,0)

    def draw(self, screen):
        screen.blit(self.surface,(self.x,self.y))
        self.surface.fill(self.color)

    def fill(self,color):
        self.color = color

