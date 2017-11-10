from Command import Command
from Position import Position
from Config import Config

iConfig = Config()
class Game():

   def placeToyRobot(self, position):
       if iConfig.getSquareBoard().isValidPosition(position) == False:
           return False
       else:
           iConfig.setPosition(position)
           #print(iConfig.getPosition().getPositionX())

   def evaluateCommand(self,command,position):
       #print (position)
       output=None
       if ((command == Command.PLACE.name) and ((position.X<0 or position.X>4) or (position.Y<0 or position.Y>4))):
            raise Exception('Invalid Command')
       if (command)==Command.PLACE.name:
           output= self.placeToyRobot(position)
           return True
       elif command==Command.MOVE.name:
           output =self.moveRobot()
       elif command ==Command.LEFT.name:
           output=self.moveLeft()
       elif command ==Command.RIGHT.name:
           output=self.moveRight()
       elif command ==Command.REPORT.name:
            print('Current Position: '+str(iConfig.getPosition().getPositionX())+' , '+str(iConfig.getPosition().getPositionY())+' , '+iConfig.getPosition().getDirection())
       return output


   def moveRobot(self):
       from Direction import Direction
       position=iConfig.getPosition()
       #newPositon=None # declare new position

       X=position.getPositionX()
       Y=position.getPositionY()
       direction=position.getDirection()

       if direction==Direction.NORTH.name:
           Y=Y+1
       elif direction==Direction.SOUTH.name:
           Y=Y-1
       elif direction == Direction.EAST.name:
           X=X+1
       elif direction == Direction.WEST.name:
           X=X-1

       newPosition=Position(X,Y,direction)
       # Evaluate position
       if iConfig.getSquareBoard().isValidPosition(newPosition) == False:
           return False
       iConfig.setPosition(newPosition)
       return True

   def moveLeft(self):
       from Direction import Direction
       #newDirection=Direction()
       position=iConfig.getPosition()
       currentDirection=position.getDirection()
       if currentDirection==Direction.NORTH.name:
          newDirection=Direction.WEST.name
       elif currentDirection==Direction.WEST.name:
          newDirection=Direction.SOUTH.name
       elif currentDirection == Direction.SOUTH.name:
          newDirection = Direction.EAST.name
       elif currentDirection==Direction.EAST.name:
          newDirection=Direction.NORTH.name

       position.setDirection(newDirection)
       iConfig.setPosition(position)
       #print('LeftPos:'+str(position.getPositionX())+str(position.getPositionY())+str(position.getDirection()))
       return True

   def moveRight(self):
       from Direction import Direction
       #newDirection = Direction()
       position = iConfig.getPosition()
       currentDirection = position.getDirection()
       if currentDirection == Direction.NORTH.name:
           newDirection = Direction.EAST.name
       elif currentDirection == Direction.EAST.name:
           newDirection = Direction.SOUTH.name
       elif currentDirection == Direction.SOUTH.name:
           newDirection = Direction.WEST.name
       elif currentDirection == Direction.WEST.name:
           newDirection = Direction.NORTH.name

       position.setDirection(newDirection)
       iConfig.setPosition(position)
       #print('RightPos:' + str(position.getPositionX()) + str(position.getPositionY()) + str(position.getDirection()))
       return True


