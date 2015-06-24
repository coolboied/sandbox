import pygame
from UiMouseArea import *
from UiImage import *
class UiImageButton(UiMouseArea,UiImage):
    def __init__(self, x=0,y=0,height=0,weight=0):
        UiMouseArea.__init__(self,x,y,height,weight)
        UiImage.__init__(self,x,y,height,weight)

