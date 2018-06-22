
class Game:

    def __init__(self):
        """
        These variables instantiate the different positions on the board via this naming convention:

        First letter: outer (o), middle (m), inner (i) refers to which ring the position is located at
        Second letter: corner (c) or middle (m), refers to whether it's a corner position or middle one
        Third letter: Top (T), Right (R), Bottom (B), Left (L) refers to where on the ring the position is located
        Fourth letter Left (L), Right (R) is only added for corner positions.

        Examples:
            imL ---> inner (ring), middle, Left position
            ocBR ---> outer, corner, Bottom-Right position

        """
        # outer ring
        self.ocTL = ' '
        self.ocTR = ' '
        self.ocBR = ' '
        self.ocBL = ' '

        self.omT = ' '
        self.omR = ' '
        self.omB = ' '
        self.omL = ' '

        # middle ring
        self.mcTL = ' '
        self.mcTR = ' '
        self.mcBR = ' '
        self.mcBL = ' '

        self.mmT = ' '
        self.mmR = ' '
        self.mmB = ' '
        self.mmL = ' '

        # inner ring
        self.icTL = ' '
        self.icTR = ' '
        self.icBR = ' '
        self.icBL = ' '

        self.imT = ' '
        self.imR = ' '
        self.imB = ' '
        self.imL = ' '

        '''This dictionary is used for a better user experience, so that they don't need to 
        deal with the strange naming that makes the programming easier. '''
        self.board = {
            1: self.ocTL,
            3: self.ocTR,
            24: self.ocBR,
            22: self.ocBL,
            2: self.omT,
            15: self.omR,
            23: self.omB,
            10: self.omL,


            4: self.mcTL,
            6: self.mcTR,
            21: self.mcBR,
            19: self.mcBL,
            5: self.mmT,
            14: self.mmR,
            20: self.mmB,
            11: self.mmL,


            7: self.icTL,
            9: self.icTR,
            18: self.icBR,
            16: self.icBL,
            8: self.imT,
            13: self.imR,
            17: self.imB,
            12: self.imL,
        }

        self.whosturn = 'Player 1'
        self.player1 = 'Player 1'
        self.player2 = 'Player 2'

        self.whitePieces = 9
        self.blackPieces = 8

        self.turnFlip = False

        self.piece = ''

        self.positions = list(range(1, 25))

        self.pieces = ['W', 'B']

        self.playingNormal = False

        self.wcounter = 1
        self.bcounter = 1

        # This dictionary allows for efficient checking of for three in a row
        self.tripleDictionary = {
            1: [(1, 2, 3), (1, 10, 22)],
            2: [(1, 2, 3), (2, 5, 8)],
            3: [(1, 2, 3), (3, 15, 24)],
            4: [(4, 5, 6), (4, 11, 19)],
            5: [(4, 5, 6), (2, 5, 8)],
            6: [(4, 5, 6), (6, 14, 21)],
            7: [(7, 8, 9), (7, 12, 16)],
            8: [(2, 5, 8), (7, 8, 9)],
            9: [(7, 8, 9), (9, 13, 18)],
            10: [(10, 11, 12), (1, 10, 22)],
            11: [(10, 11, 12), (4, 11, 19)],
            12: [(10, 11, 12), (7, 12, 16)],
            13: [(13, 14, 15), (9, 13, 18)],
            14: [(13, 14, 15), (6, 14, 21)],
            15: [(13, 14, 15), (3, 15, 24)],
            16: [(16, 17, 18), (7, 12, 16)],
            17: [(16, 17, 18), (17, 20, 23)],
            18: [(16, 17, 18), (9, 13, 18)],
            19: [(19, 20, 21), (4, 11, 19)],
            20: [(19, 20, 21), (17, 20, 23)],
            21: [(19, 20, 21), (6, 14, 21)],
            22: [(22, 23, 24), (1, 10, 22)],
            23: [(22, 23, 24), (17, 20, 23)],
            24: [(22, 23, 24), (3, 15, 24)]
        }

        self.movement = {
            1: [2, 10],
            2: [1, 3, 5],
            3: [2, 15],
            4: [11, 5],
            5: [2, 4, 6, 8],
            6: [5, 14],
            7: [8, 12],
            8: [5, 7, 9],
            9: [8, 13],
            10: [1, 11, 22],
            11: [4, 10, 11, 12, 19],
            12: [7, 11, 16],
            13: [9, 14, 18],
            14: [6, 13, 15, 21],
            15: [3, 14, 24],
            16: [12, 17],
            17: [16, 18, 20],
            18: [13, 17],
            19: [11, 20],
            20: [19, 21],
            21: [14, 20],
            22: [10, 23],
            23: [22, 20, 23],
            24: [15, 23]
        }

    def showboard(self):
        print(f"{self.board[1]}---------------{self.board[2]}---------------{self.board[3]}  1---------------2-------"
              f"--------3")
        print('|               |               |  |               |               |')
        print('|               |               |  |               |               |')
        print(f"|    {self.board[4]}----------{self.board[5]}----------{self.board[6]}    |  |    4----------5--------"
              f"--6    |")
        print('|    |          |          |    |  |    |          |          |    |')
        print('|    |          |          |    |  |    |          |          |    |')
        print(f"|    |    {self.board[7]}-----{self.board[8]}-----{self.board[9]}    |    |  |    |    7-----8-----9   "
              f" |    |")
        print('|    |    |           |    |    |  |    |    |           |    |    |')
        print('|    |    |           |    |    |  |    |    |           |    |    |')
        print(f'{self.board[10]}----{self.board[11]}----{self.board[12]}           {self.board[13]}----{self.board[14]}'
              f'----{self.board[15]}  10---11---12          13---14---15')
        print('|    |    |           |    |    |  |    |    |           |    |    |')
        print('|    |    |           |    |    |  |    |    |           |    |    |')
        print(f'|    |    {self.board[16]}-----{self.board[17]}-----{self.board[18]}    |    |  |    |    16----17---'
              f'-18   |    |')
        print('|    |          |          |    |  |    |          |          |    |')
        print('|    |          |          |    |  |    |          |          |    |')
        print(f'|    {self.board[19]}----------{self.board[20]}----------{self.board[21]}    |  |    19---------20----'
              f'-----21   |')
        print('|               |               |  |               |               |')
        print('|               |               |  |               |               |')
        print(f'{self.board[22]}---------------{self.board[23]}---------------{self.board[24]}  22--------------23---'
              f'-----------24')
        return

    def switchturn(self):

        if not self.turnFlip:
            self.turnFlip = True
            self.piece = 'W'
            self.whosturn = self.player1
            if not self.playingNormal:
                self.whitePieces -= 1
            return self.whosturn
        else:
            self.turnFlip = False
            self.piece = 'B'
            self.whosturn = self.player2
            if not self.playingNormal:
                self.blackPieces -= 1
            print(f'blacks: {self.blackPieces} whites: {self.whitePieces}')
            return self.whosturn

    def takeoutposition(self):
        while True:
            print(f"It is {self.whosturn}'s turn! Place your piece on the board")
            while True:
                try:
                    position = input()
                    self.positions.remove(int(position))
                    break
                except ():
                    print('Error! You there already is a piece there. try another position')
            self.board[int(position)] = self.piece
            self.checktriple(position)
            self.showboard()
            self.switchturn()
            if self.whitePieces == 0 and self.blackPieces == 0:
                self.playingNormal = True
                break

    def openingphase(self):
        self.switchturn()
        while self.whitePieces and self.blackPieces != 0:
            self.takeoutposition()

    def killpiece(self):
        print("You've made a mill! Good job! Choose one of the opponents pieces to be taken off the board.")
        while True:
            piece = int(input())
            if self.board[piece] == self.piece:
                print("You can't pick your own piece! Choose one of your opponents pieces.")
            elif self.board[piece] == ' ':
                print("You can't pick an empty spot! Choose a spot with your opponents piece.")
            elif self.board[self.tripleDictionary[piece][0][0]] == self.board[self.tripleDictionary[piece][0][1]] and \
                    self.board[self.tripleDictionary[piece][0][1]] == self.board[self.tripleDictionary[piece][0][2]]:
                print("(horizontal) You can't pick an opponents piece that is in a mill! Choose another piece")
            elif self.board[self.tripleDictionary[piece][1][0]] == self.board[self.tripleDictionary[piece][1][1]] and \
                    self.board[self.tripleDictionary[piece][1][1]] == self.board[self.tripleDictionary[piece][1][2]]:
                print("(vertical) You can't pick an opponents piece that is in a mill! Choose another piece")
            else:
                if self.board[piece] == 'W':
                    self.whitePieces += 1
                else:
                    self.blackPieces += 1
                self.positions.append(piece)
                self.board[piece] = ' '
                break
        return

    def checktriple(self, position):
        for postuple in self.tripleDictionary[int(position)]:
            if self.board[postuple[0]] == self.board[postuple[1]] and self.board[postuple[1]] == \
                    self.board[postuple[2]]:
                self.killpiece()
                return
        return

    def checkstatus(self):
        wcounter = 1
        bcounter = 1
        for attr, value in self.board.items():
            if value == 'W':
                wcounter += 1
            elif value == 'B':
                bcounter += 1
        print('wcounter: ' + str(wcounter) + ' bcounter: ' + str(bcounter))
        if self.piece == 'W' and wcounter <= 3:
            return True
        elif self.piece == 'B' and bcounter <= 3:
            return True
        return False

    def move(self):
        while True:
            piece = int(input(f"It is {self.whosturn}'s turn. Pick a piece you want to move.\n"))
            if self.board[piece] == self.piece:
                self.board[piece] = ' '
                break
            print("That's not your piece! Try again.")
        while True:
            position = int(input("Pick a spot where you would like to place it"))
            if self.board[position] == ' ':
                if self.checkstatus():
                    self.board[position] = self.piece
                    self.checktriple(position)
                    break
                elif piece in self.movement[position]:
                    self.board[position] = self.piece
                    self.checktriple(position)
                    break
            print("That's an invalid position! Try again.")
        self.showboard()
        self.checkstatus()

    def checkwin(self):
        wcounter = 0
        bcounter = 0
        for attr, value in self.board.items():
            if value == 'W':
                wcounter += 1
            elif value == 'B':
                bcounter += 1
        if wcounter < 3 or bcounter < 3:
            return True
        else:
            return False

    def playingphase(self):
        print(f"Welcome to the normal playing phase! It is {self.whosturn}'s turn. Move your pieces along the lines "
              f"to try and get more mills. Good luck!")
        while True:
            self.move()
            if self.checkwin():
                break
            self.switchturn()

    def finalremarks(self):
        print(f"Congratulations {self.whosturn}! You have won!")

    def play(self):
        self.showboard()
        self.openingphase()
        self.playingphase()
        self.finalremarks()


gameTime = Game()
gameTime.play()
