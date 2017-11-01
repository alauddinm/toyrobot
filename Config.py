from SquareBoard import SquareBoard
from ToyRobot import ToyRobot
from Position import Position
from GlobalPosition import GlobalPosition

class Config():
    def __init__(self):
        self.squareBoard = SquareBoard(4, 4)  # Row, Col, validPosition
        self.toyRobot = ToyRobot(Position(0, 0, "NORTH"))  # move, rotate left & right

    def getSquareBoard(self):
        return self.squareBoard

    def getToyRobot(self):
        return self.toyRobot

    def setPosition(self, position):
        self.position = position

    def getPosition(self):
        return self.position