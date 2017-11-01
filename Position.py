
class Position():
    def __init__(self,X,Y,direction):
        self.X=int(X)
        self.Y=int(Y)
        self.direction=direction

    def change(self,xNew,yNew):
        self.X=self.X+xNew
        self.X=self.Y+yNew

    def getNextPosition(self):
        if self.direction==None:
           raise Exception('Wrong Direction')
        position=Position()
      #  if self.direction==Command.

    def getPositionX(self):
        return self.X

    def setPositionX(self,X):
        self.X=X

    def getPositionY(self):
        return self.X

    def setPositionY(self,X):
        self.X=X

    def getDirection(self):
        return self.direction

    def setDirection(self,direction):
        self.direction=direction

