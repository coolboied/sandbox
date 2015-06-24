import pygame
from UiMouseArea import *
from UiObject import *
class UiButton(UiMouseArea,UiObject):
    def __init__(self, x=0,y=0,height=0,weight=0):
        UiMouseArea.__init__(self,x,y,height,weight)
        UiObject.__init__(self,x,y,height,weight)

