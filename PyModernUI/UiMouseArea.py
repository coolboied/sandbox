from UiArea import *
class UiMouseArea(UiArea):
    def __init__(self, x=0,y=0,height=0,weight=0):
        UiArea.__init__(self,x,y,height,weight)
        self.mouse_down_callback = None
        self.mouse_up_callback = None
        self.click_call_back = None

    def onMouseDown(self, callback, parameter):
        self.mouse_down_callback = callback
        self.mouse_down_parameter = parameter

    def onMouseUp(self, callback, parameter):
        self.mouse_up_callback = callback
        self.mouse_up_parameter = parameter

    def onClick(self,call_back, parameter):
        self.click_call_back = call_back
        self.click_parameter = parameter
    
    def mouseDown(self):
        if self.mouse_down_callback:
            self.mouse_down_callback(self, self.mouse_down_parameter)
        self.is_mouse_down = True

    def mouseUp(self):
        if self.mouse_up_callback:
            self.mouse_up_callback(self, self.mouse_up_parameter)

        if self.is_mouse_down:
            self.cliced()

        self.is_mouse_down = False 

    def renew(self):
        self.is_mouse_down = False

    def cliced(self):
        if self.click_call_back:
            self.click_call_back(self, self.click_parameter)
