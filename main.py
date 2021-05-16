
class TicTac:
    '''A simple command line Tic Tac Toe game. To start run: python -m main'''
    def __init__(self, board, active=True):
        self.board = board
        self.active = active
        self.player = 'X'
        

    def showBoard(self):
        '''Show the Tic Tac Toe board, incl. fields occupied by a players icon.'''
        print("\n", "Tic Tac Toe - The Game", "\n")
        print(self.board[1], " | ", self.board[4], " | ", self.board[7])
        print(self.board[2], " | ", self.board[5], " | ", self.board[8])
        print(self.board[3], " | ", self.board[6], " | ", self.board[9])
        print("\n")
    
    def playRound(self):
        '''Ask a player to do a move, by choosing an unoccupied field.
        The field can be choosen by entering the accossiated field ID.'''
        
        while True:
            print("Player", self.player)
            move = input("Please, enter a field ID for your next move.")
            if move == 'q':
                self.active = False
                return
            try:
                move = int(move)
            except ValueError:
                print("Please enter ID between 1 and 9")
            else:
                if move >= 1 and move <= 9:
                    if self.board[move] == "X" or self.board[move] == "O":
                        print("Field is already occupied!")
                    else:
                        self.board[move] = self.player
                        self.showBoard()
                        fin = self.gameOver()
                        if fin:
                            print("Game over!", "Player", self.player, "wins!")
                            self.active = False
                        fin = self.remis()
                        if fin=='remis':
                            print("Game over!", "Remis!")
                            self.active = False
                        self.updatePlayer()
                        return move
                else:
                    print("ID must be a number between 1 and 9")

    def updatePlayer(self):
        '''Automatic change of players for every turn'''
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'
    
    def gameOver(self):
        if self.board[1] == self.board[2] == self.board[3]:
            return self.board[1]
        if self.board[4] == self.board[5] == self.board[6]:
            return self.board[4]        
        if self.board[7] == self.board[8] == self.board[9]:
            return self.board[7]
        if self.board[1] == self.board[4] == self.board[7]:
            return self.board[1]
        if self.board[2] == self.board[5] == self.board[8]:
            return self.board[2]
        if self.board[3] == self.board[6] == self.board[9]:
            return self.board[3]
        if self.board[1] == self.board[5] == self.board[9]:
            return self.board[1]
        if self.board[3] == self.board[5] == self.board[7]:
            return self.board[3]

    def remis(self):
        if (self.board[1] == 'X' or self.board[1] == 'O') \
            and (self.board[2] == 'X' or self.board[2] == 'O') \
            and (self.board[3] == 'X' or self.board[3] == 'O') \
            and (self.board[4] == 'X' or self.board[4] == 'O') \
            and (self.board[5] == 'X' or self.board[5] == 'O') \
            and (self.board[6] == 'X' or self.board[6] == 'O') \
            and (self.board[7] == 'X' or self.board[7] == 'O') \
            and (self.board[8] == 'X' or self.board[8] == 'O') \
            and (self.board[9] == 'X' or self.board[9] == 'O'):
                return ('remis')

def main():
    bSize = [*range(11)]
    play = TicTac(bSize, True)
    play.showBoard()
    while play.active == True:
        play.playRound()

if __name__ == "__main__":main()