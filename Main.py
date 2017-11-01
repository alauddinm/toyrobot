import argparse
from Game import Game
from Position import Position
from Config import Config

from SquareBoard import SquareBoard
from GlobalPosition import GlobalPosition

# self.squareBoard = SquareBoard(4, 4)  # Row, Col, validPosition
# self.toyRobot = ToyRobot()  # move, rotate left & right
# self.game = Game(self.squareBoard, self.toyRobot)  # decide on which command to  execute & report

parser=argparse.ArgumentParser()
parser.add_argument("command",help="Command")
parser.add_argument("originX",help="X coordinate")
parser.add_argument("originY",help="Y coordinate")
parser.add_argument("direction",help="Direction")
args=parser.parse_args()


keepRunning = True
while (keepRunning):
 #inputString = args
#inputString='PLACE 2,3,NORTH'
    if args.command=="exit":
        keepRunning = False
    else:
        #print (args)
        if ((args.originX) and (args.originY) and (args.direction)) :
            originX = args.originX
            originY = args.originY
            direction = args.direction
            command=str(args.command).upper()
            args.originX = ""
            args.originY = ""
            args.direction = ""
            position = Position(originX, originY, str(direction).upper())  # X,Y, Direction
            Config().setPosition(position)

        else:
            command = raw_input("Command: ")
            command=command.upper()


        outputVal=Game().evaluateCommand(command,position)
        #print(outputVal)

           #outputval=game.eval(args.command,args.originX,args.originY,args.direction)
#if __name__ == "__main__":