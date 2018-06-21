
class Game:

    def __init__(self):

        '''
        These variables instantiate the different positions on the board via this naming convention:

        First letter: outer (o), middle (m), inner (i) refers to which ring the position is located at
        Second letter: corner (c) or middle (m), refers to whether it's a corner position or middle one
        Third letter: Top (T), Right (R), Bottom (B), Left (L) refers to where on the ring the position is located
        Fourth letter Left (L), Right (R) is only added for corner positions.

        Examples:
            imL ---> inner (ring), middle, Left position
            ocBR ---> outer, corner, Bottom-Right position
        '''
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

        '''This ditionary is used for a better user experience, so that they don't need to 
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

        self.whosturn = 'dunno'
        self.player1 = 'Player 1'
        self.player2 = 'Player 2'

        self.whitePieces = 5
        self.blackPieces = 4

        self.turnFlip = False

        self.piece = 'youshouldnotseethis'

        self.positions = list(range(1,25))

        self.tripleDictionary = {
            1: ((1, 2, 3), (1, 10, 22)),
            2: ((1, 2, 3), (2, 5, 8)),
            3: ((1, 2, 3), (3, 15, 24)),
            4: ((4, 5, 6), (4, 11, 19)),
            5: ((4, 5, 6), (2, 5, 8)),
            6: ((4, 5, 6), (6, 14, 21)),
            7: ((7, 8, 9), (7, 12, 16)),
            8: ((2, 5, 8), (7, 8, 9)),
            9: ((7, 8, 9), (9, 13, 18)),
            10: ((10, 11, 12),(1, 10, 22)),
            11: ((10, 11, 12), (4, 11, 19)),
            12: ((10, 11, 12), (7, 12, 16)),
            13: ((13, 14, 15), (9, 13, 18)),
            14: ((13, 14, 15), (6, 14, 21)),
            15: ((13, 14, 15), (3, 15, 24)),
            16: ((16, 17, 18), (7, 12, 16)),
            17: ((16, 17, 18), (17, 20, 23)),
            18: ((16, 17, 18), (9, 13, 18)),
            19:
        }


    def placementBeginning(self):
        print('Type in the number where you want to place the piece at');
        return

    def placementDocumentation(self):
        self.placementBeginning()
        print('1---------------2---------------3')
        print('|               |               |')
        print('|               |               |')
        print('|    4----------5----------6    |')
        print('|    |          |          |    |')
        print('|    |          |          |    |')
        print('|    |    7-----8-----9    |    |')
        print('|    |    |           |    |    |')
        print('|    |    |           |    |    |')
        print('10---11---12          13---14---15')
        print('|    |    |           |    |    |')
        print('|    |    |           |    |    |')
        print('|    |    16----17----18   |    |')
        print('|    |          |          |    |')
        print('|    |          |          |    |')
        print('|    19---------20---------21   |')
        print('|               |               |')
        print('|               |               |')
        print('22--------------23--------------24')
        return

    def showBoard(self):
        print(f"{self.board[1]}---------------{self.board[2]}---------------{self.board[3]}")
        print('|               |               |')
        print('|               |               |')
        print(f"|    {self.board[4]}----------{self.board[5]}----------{self.board[6]}    |")
        print('|    |          |          |    |')
        print('|    |          |          |    |')
        print(f"|    |    {self.board[7]}-----{self.board[8]}-----{self.board[9]}    |    |")
        print('|    |    |           |    |    |')
        print('|    |    |           |    |    |')
        print(f'{self.board[10]}----{self.board[11]}----{self.board[12]}           {self.board[13]}----{self.board[14]}----{self.board[15]}')
        print('|    |    |           |    |    |')
        print('|    |    |           |    |    |')
        print(f'|    |    {self.board[16]}-----{self.board[17]}-----{self.board[18]}    |    |')
        print('|    |          |          |    |')
        print('|    |          |          |    |')
        print(f'|    {self.board[19]}----------{self.board[20]}----------{self.board[21]}    |')
        print('|               |               |')
        print('|               |               |')
        print(f'{self.board[22]}---------------{self.board[23]}---------------{self.board[24]}')
        return

    def switchTurn(self):

        if self.turnFlip == False:
            self.turnFlip = True
            self.piece = 'W'
            self.whosturn = self.player1
            self.whitePieces -= 1
            print(f'blacks: {self.blackPieces} whites: {self.whitePieces}')
            return self.whosturn
        else:
            self.turnFlip = False
            self.piece = 'B'
            self.whosturn = self.player2
            self.blackPieces -= 1
            print(f'blacks: {self.blackPieces} whites: {self.whitePieces}')
            return self.whosturn

    def takeoutposition(self):
        while True:
            try:
                position = input(f"It is {self.whosturn}'s turn! Place your piece on the board")
                self.positions.remove(int(position))
                self.board[int(position)] = self.piece
                self.showBoard()
                self.switchTurn()
                if self.whitePieces == 0 and self.blackPieces == 0:
                    break
            except:
                print('Error! You there already is a piece there. try another position')


    def openingPhase(self):
        while self.whitePieces and self.blackPieces != 0:
            self.takeoutposition()

    def checkTriple(self):



    def play(self):
        self.placementDocumentation()
        self.openingPhase()



gameTime = Game()
gameTime.play()


# gameTime.showBoard()
# gameTime.placementDocumentation()

