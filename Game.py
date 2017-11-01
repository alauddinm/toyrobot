from Command import Command
from Position import Position
from SquareBoard import SquareBoard
from GlobalPosition import GlobalPosition
from Config import Config

#Class Game():
#def __init__():
iConfig = Config()
class Game():
   '''def __init__(self,command,X,Y,direction):
       self.X = X
       self.Y = Y
       self.direction = direction'''
    #self.command=command

   def placeToyRobot(self, position):
       if iConfig.getSquareBoard().isValidPosition(position) == False:
           return False
       else:
           iConfig.setPosition(position)
           print(iConfig.getPosition().getPositionX())


   def evaluateCommand(self,command,position):
       #print (position)
      # if ((command == Command.PLACE.name) and ((position.X<0 or position.X>4) or (position.Y<0 or position.Y>4))):
       #     raise Exception('Invalid Command')
       if (command)==Command.PLACE.name:

           output= self.placeToyRobot(position)

       elif command==Command.MOVE.name:
            print('Move')
       elif command ==Command.LEFT.name:
            print('Left')
       elif command ==Command.RIGHT.name:
            print('Right')
       elif command ==Command.REPORT.name:
            print('Current Position: '+str(iConfig.getPosition().getPositionX())+' , '+str(iConfig.getPosition().getPositionY())+' , '+iConfig.getPosition().getDirection())





    #validate PLACE params


