class Transform:
    def __init__(self, callBack, obj, transFrom, transTo, inStep):
        self.callBack = callBack
        self.obj = obj
        self.transFrom = transFrom
        self.transTo = transTo
        self.inStep = inStep
        self.step = 0 

    def play(action):
        transValueNow = float((action.transTo - action.transFrom))/float(action.inStep)*float(action.step) + action.transFrom
        action.callBack(action.obj,transValueNow)
        action.step = action.step+1
        if action.step > action.inStep:
            action.step = 0
            return True
        return False

