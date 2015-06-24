from Transform import *
class MoveAction:

    @staticmethod 
    def moveX(area, moveFrom, moveTo, inStep):
        def setX(area,x):
            area.x = x
        transform = Transform(setX, area, moveFrom, moveTo, inStep)
        return transform

    @staticmethod 
    def moveY(area, moveFrom, moveTo, inStep):
        def setY(area,x):
            area.y = y
        transform = Transform(setY, area, moveFrom, moveTo, inStep)
        return transform

    @staticmethod 
    def movePos(area, moveFrom, moveTo, inStep):
        (fromX, fromY)=moveFrom
        (toX,toY) = moveTo

        def moveStep(area,step):
            x = float(toX-fromX)/float(inStep)*float(step)+float(fromX)
            y = float(toY-fromY)/float(inStep)*float(step)+float(fromY)
            area.x = x
            area.y = y

        transform = Transform(moveStep, area, 1, inStep, inStep)
        return transform



