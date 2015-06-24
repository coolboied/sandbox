import pygame
from pygame.locals import *
from UiObject import *
from UiMouseArea import *
class UiCanvas(UiObject):
    def __init__(self, x=0,y=0,height=0,weight=0):
        UiObject.__init__(self,x,y,height,weight)
        self.children = []

    def draw(self, screen):
        for child in self.children:
            child.draw(self.surface)
        UiObject.draw(self,screen)

    def addChild(self,uiObject):
        self.children.append(uiObject)

    def eventHandle(self,event):
        if event.type==MOUSEBUTTONDOWN:
            for child in self.children:
                if isinstance(child, UiMouseArea):
                    if child.isInArea(event.pos):
                        child.mouseDown()
        elif event.type==MOUSEBUTTONUP:
            for child in self.children:
                if isinstance(child, UiMouseArea):
                    if child.isInArea(event.pos):
                        child.mouseUp()
                    else:
                        child.renew()

