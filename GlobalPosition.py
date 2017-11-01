
class GlobalPosition():
    def __init__(self,X,Y,direction):
        self.X=X
        self.Y=Y
        self.direction=direction

    def setGlobalPositionX(self,X):
        self.X=X

    def setGlobalPositionY(self,Y):
        self.Y=Y

    def setGlobalPositionDirection(self,direction):
        self.direction=direction

    def getGlobalPositionX(self):
        return self.X

    def getGlobalPositionY(self):
        return self.Y

    def getGlobalPositionDirection(self):
        return self.direction

