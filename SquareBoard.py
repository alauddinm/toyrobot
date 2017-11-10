from Position import Position
from GlobalPosition import GlobalPosition

class SquareBoard():
    def __init__(self,rows,columns):
        self.rows=rows
        self.columns=columns
        #print('squareBorad Init: ' + str(self.rows) + ', ' + str(self.columns))

    def getRows(self):
        return self.rows

    def setRows(self, rows):
        self.rows= rows

    def getColumns(self):
        return self.columns

    def setColumns(self, columns):
        self.columns= columns

    def isValidPosition(self,position):
        #print(position.getPositionX()+position.getPositionY()+self.getRows()+self.getColumns())
        return (position.getPositionX()<=int(self.getColumns()) and position.getPositionX()>=0 and position.getPositionY()<=int(self.getRows()) and position.getPositionY()>=0)


