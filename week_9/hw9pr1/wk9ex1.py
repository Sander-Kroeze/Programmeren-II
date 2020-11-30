#
# hw9pr1.py - Game of Life lab
#
# Name: Sander kroeze & Chris Wibbelink
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
    
def diagonalize(width, height):
    """Creates an empty board and then modifies it
       so that it has a diagonal strip of "on" cells.
       But do that only in the *interior* of the 2D array.
    """
    a = create_board(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if row == col:
                a[row][col] = 1
            else:
                a[row][col] = 0

    return a

def inner_cells(w, h):
    """
        Creats a board with only the number 1 in the centre.
        On the outside of the board only the number 0.
    """
    a = create_board(w, h)

    for row in range(h):
        for col in range(w):
            if 0 < row < h - 1 and 0 < col < w - 1:
                a[row][col] = 1
            else:
                a[row][col] = 0

    return a

def random_cells(w, h):
    """"
        Creats a board with random numbers.
        But only the first and the last row can't be changed
    """
    a = create_board(w, h)

    for row in range(h):
        for col in range(w):
            if 0 < row < h - 1 and 0 < col < w - 1:
                a[row][col] = random.choice([0, 1])
            else:
                a[row][col] = 0
    
    return a

def copy(a):
    """Returns a DEEP copy of the 2D array a."""
    height = len(a)
    width = len(a[0])
    new_a = create_board(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            new_a[row][col] = a[row][col]

    return new_a

def inner_reverse(a):
    """
        Creats a board form another board, 
        but the 1 and 0 in the board are turn around
        exept for the outherline.
    """
    for row in range(len(a)):
        for col in range(len(a[0])):
            if 0 < row < len(a) - 1 and 0 < col < len(a[0]) -1:
                a[row][col] = (a[row][col] + 1) % 2
            else:
                a[row][col] = 0

    return a

def count_neighbours(row, col, a):
    count = 0

    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            if abs(x) + abs(y) != 0:
                count += a [row + x][col + y]
    return count

def next_life_generation(a):
    """Makes a copy of a and then advances one
       generation of Conway's Game of Life within
       the *inner cells* of that copy.
       The outer edge always stays at 0.
    """
    w = len(a[0])
    h = len(a)
    new_a = create_board(w, h)

    for n in range(h):
        for m in range(w):
            if 0 < n < h - 1 and 0 < m < w - 1:
                count = count_neighbours(n, m, a)
                if count < 2 or count > 3:
                    new_a [n][m] = 0
                elif count == 3:
                    new_a[n][m] =1
                else:
                    new_a[n][m] = a[n][m]
            else:
                new_a[n][m] = 0
    
    return new_a



















