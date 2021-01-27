import random

class Board:
    def __init__ (self, width, height) :
        """Construct a player for a given checker, tie-breaking type,
           and ply."""
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [[' '] * W for row in range(H)]

    def __repr__ (self) :
        """Create a string represenation of the player."""
        H = self.height
        W = self.width
        s = '\n'   
        for row in range(0, H):
            s += '|'

            for col in range(0, W):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2 * W + 1) * '-'    
        s += '\n'
        for col in range(0, W) :
            s += " " + str(col%10)
        
        return s + "\n"       #returnd het board

    def add_move(self, col, ox):
        """
            Met deze functie wordt er een zet gezet zonder dat er gecontoleerd wordt of de zet wel in het board past
        """
        for i in range (0, self.height):

            if self.data[i][col] != " " :
                self.data[i - 1][col] = ox
                return None

        self.data[self.height - 1][col] = ox

    def clear(self):
        """
            Zorgt er voor dat het board weer leeg gemaakt wordt.
        """
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
        """
            geeft een True or False waarde terug om te kijken of je zet is toegestaan
        """
        if col < 0 or col >= self.width :
            return False

        if self.data[0][col] != ' ' :

            return False
        return True

    def is_full(self):
        """"
            Kijkt of het board vol zit
        """
        for i in self.data :
            for j in i :
                if j == ' ' :
                    return False
        return True

    def del_move(self, col):
        """"
            Deze functie verwijderd de laaste zet 
        """
        for i in range(self.height) :
            if self.data[i][col] != ' ':
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
    
    def host_game(self):
        """
            Hier mee begin je het spel vier op een rij.
            door in de while loop 'not' toe te voegen hoef je daar geen input te geven.
        """
        print("Welkom bij Vier op een rij!")
        print(self)
        while True :
            users_col = -1
            while not self.allows_move( users_col ) == False:
                users_col = int(input("Keuze van X: ")) #domme keuzes van de computer
            self.add_move(users_col, "X")
            print(self)
            \
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
    
class Player:
    """An AI player for Connect Four."""

    def __init__(self, ox, tbt, ply):
        """Construct a player for a given checker, tie-breaking type,
           and ply."""
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__(self):
        """Create a string represenation of the player."""
        s = "Player: ox = " + self.ox + ", "
        s += "tbt = " + self.tbt + ", "
        s += "ply = " + str(self.ply)
        return s
    
    def opp_ch(self):
        """
            Deze methode geeft de andere steen terug.
        """
        return 'O' if self.ox == 'X' else 'X'
    
    def score_board(self, b):
        """"
            Deze methode geeft float-waardes terug, op basis van de invoer van b
            100.0 als het gewonnen is door self, 50.0 al sself niet gewonnen of verloren heeft
            en 0.0 als self verloren heeft.
        """
        user_wint = b.wins_for(self.ox)
        opp_wint = b.wins_for(self.opp_ch())

        if user_wint :
            return 100.0
        elif opp_wint :
            return 0.0
        else :
            return 50.0
    
    def tiebreak_move(self, scores) :
        max_indices = -10

        for score in scores :
            if score > max_indices :
                max_indices = score

        ls = []

        for i in range(len(scores)) :
            if scores[i] == max_indices :
                ls.append(i)

        if self.tbt == 'LEFT' :
            return ls[0]
        elif self.tbt == 'RIGHT' :
            return ls[-1]
        else :
            return random.choice(ls)

    def scores_for(self, b) :
        ls = [self.score_board(b)] * b.width

        for i in range(b.width) :
            if not b.allows_move(i) :
                ls[i] = -1
            elif self.ply != 0 :
                b.add_move(i, self.ox)
                score = self.score_board(b)
                if score == 100.0 :
                    ls[i] = 100.0
                else :
                    opp = Player(self.opp_ch(), self.tbt, self.ply-1)
                    bestOpp = max(opp.scores_for(b))
                    ls[i] = 100.0 - bestOpp
                b.del_move(i)
                
        return ls

# Test voor opp_ch(self)
p = Player('X', 'LEFT', 3)
assert p.opp_ch() == 'O'
assert Player('O', 'LEFT', 0).opp_ch() == 'X'

# Test voor score_board(self, b)
b = Board(7, 6)
b.set_board('01020305')
print(b)
p = Player('X', 'LEFT', 0)
assert p.score_board(b) == 100.0
assert Player('O', 'LEFT', 0).score_board(b) == 0.0
assert Player('O', 'LEFT', 0).score_board(Board(7, 6)) == 50.0

#Test voor tiebreakmove
scores = [0, 0, 50, 0, 50, 50, 0]
p = Player('X', 'LEFT', 1)
p2 = Player('X', 'RIGHT', 1)
p3 = Player('X', 'RANDOM', 1)
assert p.tiebreak_move(scores) == 2
assert p2.tiebreak_move(scores) == 5
assert p3.tiebreak_move(scores) in [2, 4, 5]

#test voor scores_for
b = Board(7, 6)
b.set_board('1211244445')
print(b)
# 0-ply lookahead ziet geen bedreigingen
assert Player('X', 'LEFT', 0).scores_for(b) == [50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0]

# 1-ply lookahead ziet een manier om te winnen
# (als het de beurt van 'O' was!)
assert Player('O', 'LEFT', 1).scores_for(b) == [50.0, 50.0, 50.0, 100.0, 50.0, 50.0, 50.0]

# 2-ply lookahead ziet manieren om te verliezen
# ('X' kan maar beter in kolom 3 spelen...)
assert Player('X', 'LEFT', 2).scores_for(b) == [0.0, 0.0, 0.0, 50.0, 0.0, 0.0, 0.0]

# 3-ply lookahead ziet indirecte overwinningen
# ('X' ziet dat kolom 3 een overwinning oplevert!)
assert Player('X', 'LEFT', 3).scores_for(b) == [0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0]

# Bij 3-ply ziet 'O' nog geen gevaar
# als hij in een andere kolom speelt
assert Player('O', 'LEFT', 3).scores_for(b) == [50.0, 50.0, 50.0, 100.0, 50.0, 50.0, 50.0]

# Maar bij 4-ply ziet 'O' wel het gevaar!
# weer jammer dat het niet de beurt van 'O' is...
assert Player('O', 'LEFT', 4).scores_for(b) == [0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0]
