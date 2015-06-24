class Animation:
    
    def __init__(self):
        self.playList = []
        self.loop =  False
        self.step = 0

    def addAction(self, action):
        self.playList.append(action)

    def play(self):
        if len(self.playList) <= self.step:
            return;
        action = self.playList[self.step]
        playOver = action.play()
        if playOver:
            self.step = self.step + 1

