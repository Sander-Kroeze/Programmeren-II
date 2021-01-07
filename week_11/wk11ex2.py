# wk11ex1.py
# 4 op een rij
# Door: Sander en Chris
#
#

import random

class Board:
    import random
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We hoeven niets terug te geven vanuit een constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # de string om terug te geven
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # onderkant van het bord
        s += "\n"
        
        for col in range(0, self.width):
            s += " " + str(col%10)

        # hier moeten de nummers nog onder gezet worden

        return s       # het bord is compleet, geef het terug

    def add_move(self, col, ox):
        """
            met deze functie wordt er een zet gezet zonder dat er gecontoleerd wordt of de zet wel in het board past
        """
        for i in range (0, self.height):
            if self.data[i][col] != " " :
                self.data[i-1][col] = ox
                return None
        self.data[self.height-1][col] = ox

    def clear(self):
        """
            zorgt er voor dat het board weer leeg gemaakt wordt.
        """
        self.data = [[' '] * self.width for row in range(self.height)]
    
    def set_board(self, move_string):
        """
        Accepts a string of columns and places
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
        """
            geeft een True or False waarde terug om te kijken of je zet is toegestaan
        """
        if 0 <= col < self.width:
            if self.data [0][col] == ' ':
                return True
        return False
    
    def is_full(self):
        """"
            Kijkt of het Board vol zit
        """
        for i in self.data:
            for j in i:
                if j == ' ':
                    return False
        return True
    
    def del_move(self, col):
        """
            deze functie moet de laaste zet verwijderen
        """
        for i in range(self.height):
            if self.data[i][col] != " ":
                self.data[i][col] = ' '
                return 
    
    def wins_for(self, ox):
        """"
            Deze funcite controleerd of iemand gewonnen heeft.
        """
        # Controleren op horizontale overwinningen
        for row in range(0, self.height):
            for col in range(0, self.width - 3):
                if self.data[row][col] == ox and \
                    self.data[row][col + 1] == ox and \
                    self.data[row][col + 2] == ox and \
                    self.data[row][col + 3] == ox:
                    return True

        # Controleren op Verticale overwinningen
        for row in range(0, self.height - 3):
            for col in range(0, self.width):
                if self.data[row][col] == ox and \
                    self.data[row + 1][col] == ox and \
                    self.data[row + 2][col] == ox and \
                    self.data[row + 3][col] == ox:
                    return True

       # Controleren op Diagonale overwinningen
        for row in range(0, self.height - 3):
            for col in range(0, self.width - 3):
                if self.data[row][col] == ox and \
                    self.data[row + 1][col + 1] == ox and \
                    self.data[row + 2][col + 2] == ox and \
                    self.data[row + 3][col + 3] == ox:
                    return True

        # Controleren op Diagonale overwinningen maar dan de andere kant op
        for row in range(0,self.height - 3):
            for col in range(3, self.width):
                if self.data[row][col] == ox and \
                    self.data[row + 1][col - 1] == ox and \
                    self.data[row + 2][col - 2] == ox and \
                    self.data[row + 3][col - 3] == ox:
                    return True

        return False

    def cols_to_win(self, ox):
        """ 
            geeft een lijst terug van kolommen 
            waar ox mee wint op de volgende beurt
        """
        L = []
        if ox == 'X':
            for i in range(7):
                if self.allows_move(i) == True:
                    self.add_move(i, 'X')
                    if self.wins_for('X') == True:
                        L.append(i)
                        self.del_move(i)
                    else:
                        self.del_move(i)
        elif ox == 'O':
            for i in range(7):
                if self.allows_move(i) == True:
                    self.add_move(i, 'O')
                    if self.wins_for('O') == True:
                        L.append(i)
                        self.del_move(i)
                    else:
                        self.del_move(i)
        else:
            print('Vul "X" of "O" in')
            
        return L
    
    def ai_move(self, ox):
        """
            Deze functie geeft een integer terug die een geldige
            kolom bevat om een zet te doen.
        """

        # code voor X
        LofX = []
        LofX.extend(self.cols_to_win('X'))
        
        # code voor O
        LofO = [] 
        LofO.extend(self.cols_to_win('O'))

        if ox == 'X':
            if bool(LofX) == False:
                if bool(LofO) == False:
                    for i in range(7):
                        if self.allows_move(i) == True:
                            return i
                elif bool(LofO) == True:
                    return LofO[0]
            elif bool(LofX) == True:
                    return LofX[0]
        elif ox == 'O':
            if bool(LofO) == False:
                if bool(LofX) == False:
                    for i in range(7):
                        if self.allows_move(i) == True:
                            return i
                elif bool(LofX) == True:
                    return LofX[0]
            elif bool(LofO) == True:
                    return LofO[0]
        else:
            print('Vul "X" of "O" in')

    

    def host_game(self):
        """
            Met deze functie worden alle bovenstaande functies gebruikt om het spel te maken
        """
        while True:
            print(self)
            m = self.ai_move('X')
   
            self.add_move(m,'X')
            if self.wins_for('X') == True:
                print('X wint -- Gefeliciteerd!')
                print(self)
                return
            elif self.is_full() == True:
                print('Gelijkspel board is vol!')
                print(self)
                return
            print(self)
            while True:                     
                m = int(input ('Keuze van O:'))
                if self.allows_move(m):
                    break
                else:
                    print("dit kan niet...")      
            self.add_move(m,'O')
            if self.wins_for('O') == True:
                print('O wint -- Gefeliciteerd!')
                print(self)
                return
            elif self.is_full() == True:
                print('Gelijkspel board is vol!')
                print(self)
                return
    



    
