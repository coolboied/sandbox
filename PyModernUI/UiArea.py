class UiArea:
    def __init__(self, x=0,y=0,height=0,weight=0):
        self.x = x
        self.y = y
        self.z = 0
        self.height = height
        self.weight = weight
    
    def isInArea(self,(x,y)):
        if(x>self.x and y>self.y and x<self.x+self.height and y <self.y+self.weight):
            return True
        else:
            return False

