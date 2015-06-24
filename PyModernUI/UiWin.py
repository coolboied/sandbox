import pygame
from pygame.locals import *
from UiCanvas import *
from sys import exit
class UiWin:
    
    def __init__(self, height = 640, weight = 480):
        pygame.init()

        self.screen = pygame.display.set_mode((height,weight),0,32)
        self.canvas = UiCanvas(0,0,height,weight);

        self.animationList = []

    def getAnimationList(self):
        return self.animationList
    
    def setWinName(self,name):
        pygame.display.set_caption(name)

    def getCanvas(self):
        return self.canvas

    def show(self):
        while True:
            self.canvas.draw(self.screen)

            pygame.display.update()

            for action in self.animationList:
                action.play()

            eventList = pygame.event.get()

            for event in eventList:
                self.canvas.eventHandle(event)
                if event.type == QUIT:
                    exit()

if __name__ == "__main__":
    from UiImage import *
    from UiObject import *
    from UiButton import *
    from UiImageButton import *
    from Animation import *
    from Transform import *
    from MoveAction import *

    def bu_click(button, image):
        button.x = button.x +10

    def bu_click2(button,a): 
        image.y = image.y+10

    def bu_(ima,x): 
        print x
        ima.x = x

    uiWin = UiWin()
    canvas = uiWin.getCanvas()
    animations = uiWin.getAnimationList()
    canvas.fill((255,255,255))

    image = UiImageButton(height = 100, weight = 100)

    action = Animation()
    #transform = Transform(bu_, image, 1, 100, 1000);
    transform = MoveAction.movePos(image,(1,1),(100,200),1000);
    action.addAction(transform);

    uiWin.animationList.append(action)
    
    image.set_image("b.jpg")
    canvas.addChild(image)
    button = UiButton(height= 50, weight=50)
    button.fill((0,0,0))
    button.onClick(bu_click, image)
    canvas.addChild(button)
    
    image.onClick(bu_click2,image)

    uiWin.show()
