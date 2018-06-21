
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
            23: self.ocBL,

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

        self.whitePieces = 12
        self.blackPieces = 12

        self.turnFlip = False

        self.piece = 'youshouldnotseethis'

        self.positions = list(range(1,25))
        print(self.positions)



    def placementBeginning(self):
        print('Type in the number where you want to place the piece at');
        return

    def placementDocumentation(self):
        self.placementBeginning(self)
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
        print(f"{self.ocTL}---------------{self.omT}---------------{self.ocTR}")
        print('|               |               |')
        print('|               |               |')
        print(f"|    {self.mcTL}----------{self.mmT}----------{self.mcTR}    |")
        print('|    |          |          |    |')
        print('|    |          |          |    |')
        print(f"|    |    {self.icTL}-----{self.imT}-----{self.icTR}    |    |")
        print('|    |    |           |    |    |')
        print('|    |    |           |    |    |')
        print(f'{self.omL}----{self.mmL}----{self.imL}           {self.imR}----{self.mmR}----{self.omR}')
        print('|    |    |           |    |    |')
        print('|    |    |           |    |    |')
        print(f'|    |    {self.icBL}-----{self.imB}-----{self.icBR}    |    |')
        print('|    |          |          |    |')
        print('|    |          |          |    |')
        print(f'|    {self.mcBL}----------{self.mmB}----------{self.mcBR}    |')
        print('|               |               |')
        print('|               |               |')
        print(f'{self.ocBL}---------------{self.omB}---------------{self.ocBR}')
        return

    def whosturn(self):
        if self.whitePieces == self.blackPieces:
            self.turnFlip = True
            self.piece = 'W'
            self.whosturn = self.player1
            return self.whosturn
        else:
            self.turnFlip = False
            self.piece = 'B'
            self.whosturn = self.player2
            return self.whosturn

    def takeoutposition(self, position):
        while True:
            try:
                self.positions.remove(position)
                return
            except:
                print('Error! You there already is a piece there. try another position')

    def openingPhase(self):
        while self.whitePieces and self.blackPieces != 0:
            self.showBoard(self)
            self.whosTurn()
            position = input(f"It is {self.whosturn}'s turn! Place your piece on the board")
            self.takeoutposition(position)



gameTime = Game()

# gameTime.showBoard()
# gameTime.placementDocumentation()

