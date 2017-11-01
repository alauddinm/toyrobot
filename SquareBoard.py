from Position import Position
from GlobalPosition import GlobalPosition

class SquareBoard():
    def __init__(self,rows,columns):
        self.rows=rows
        self.columns=columns
        print('squareBorad Init: ' + str(self.rows) + ', ' + str(self.columns))

    def isValidPosition(self,position):
        print (position.getPositionX())
        print( position.getPositionY())

        return (position.getPositionX()<=self.columns or position.getPositionX()>=0 or
                   position.getPositionY()<=self.rows or position.getPositionY()>=0)


