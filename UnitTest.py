from SquareBoard import SquareBoard
from GlobalPosition import GlobalPosition

class Test:

    def __init__(self, squareBoard, toyRobot, game):
        self.squareBoard = SquareBoard(4, 4)  # Row, Col, validPosition
        self.toyRobot = ToyRobot()  # move, rotate left & right
        self.game = Game(self.squareBoard, self.toyRobot)  # decide on which command to  execute & report

        print ('GlobalPostion positions updated.' )
    # print (globalPosition)