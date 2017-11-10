from SquareBoard import SquareBoard
from GlobalPosition import GlobalPosition
import re

class Test:
    input = raw_input("Command: ")
    whiteSpaceRegex = "\\s";
    position = input.split(whiteSpaceRegex);
    print (position)
    position = position.upper()

    pattern = re.compile("^\s+|\s*,\s*|\s+$")
    print([x for x in pattern.split(position) if x])