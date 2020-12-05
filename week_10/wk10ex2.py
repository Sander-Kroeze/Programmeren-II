# Door Sander Kroeze
from random import randrange
class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """
    

    def __init__ (self, width, height) :
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [[' '] * W for row in range(H)]

    def __repr__ (self) :
        """ this method returns a string representation
            for an object of type Board
        """
        H = self.height
        W = self.width
        s = '\n'   # the string to return
        for row in range(0, H):
            s += '|'   
            for col in range(0, W):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2 * W + 1) * '-'    # bottom of the board
        s += '\n'
        for col in range(0, W) :
            s += " " + str(col%10)
        
        return s + "\n"       # the board is complete, return it

    def add_move(self, col, ox):
        for i in range (0, self.height):
            if self.data[i][col] != " " :
                self.data[i - 1][col] = ox
                return None

        self.data[self.height - 1][col] = ox

    def clear(self):
        self.data = [[' '] * self.width for row in range(self.height)]

    def set_board(self, move_string):
        """Accepts a string of columns and places
        alternating checkers in those columns,
        starting with 'X'.

        For example, call b.set_board('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.set_board('000000') to
        see them alternate in the left column.

        move_string must be a string of one-digit integers.
        """
        next_checker = 'X'   # we starten door een 'X' te spelen
        for col_char in move_string:
            col = int(col_char)
            if 0 <= col <= self.width:
                self.add_move(col, next_checker)
            if next_checker == 'X':
                next_checker = 'O'
            else:
                next_checker = 'X'
    def allows_move(self, col):
        if col < 0 or col >= self.width :
            return False
        if self.data[0][col] != ' ' :
            return False
        return True

    def is_full(self):
        for i in self.data :
            for j in i :
                if j == ' ' :
                    return False
        return True

    def del_move(self, col):
        for i in range(self.height) :
            if self.data[i][col] != ' ':
                self.data[i][col] = ' '
                return
    
    def wins_for(self, ox):
        # Controleren op horizontale overwinningen
        for row in range(0, self.height):
            for col in range(0, self.width - 3):
                if self.data[row][col] == ox and \
                self.data[row][col + 1] == ox and \
                self.data[row][col + 2] == ox and \
                self.data[row][col + 3] == ox:
                    return True
        return False
    
    def host_game(self):
        print("Welkom bij Vier op een rij!")
        print(self)
        while True :
            users_col = -1
            while not self.allows_move( users_col ) == False:
                users_col = int(input("Keuze van X: ")) #domme keuzes van de computer
            self.add_move(users_col, "X")
            print(self)
            if self.wins_for("X") :
                print("X wint -- Gefeliciteerd!")
                return
            users_col = -1
            while self.allows_move(users_col) == False:
                users_col = int(input("Keuze van O: "))
            self.add_move(users_col, "O")
            print(self)
            if self.wins_for("O") :
                print("O wint -- Gefeliciteerd!")
                return
            elif self.is_full():
                print("Gelijkspel..")
                return



