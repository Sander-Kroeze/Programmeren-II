#
# hw9pr1.py - Game of Life lab
#
# Name:
#

import random

def createOneRow(width):
    """ returns one row of zeros of width "width"...  
         You might use this in your createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row

def create_board(width, height):
    """Returns a 2D array with "height" rows and "width" columns."""
    a = []
    for row in range(height):
        a += [createOneRow(width)]  # gebruik de bovenstaande functie zodat ... één rij is!!
    return a

def print_board(a):
    """This function prints the 2D list-of-lists a."""
    for row in a:               # row is de hele rij
        line = ''
        for col in row:         # col is het individuele element
            line += str(col)
        print(line)
    print




















