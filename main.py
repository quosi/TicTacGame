
class TicTac:
    '''A simple command line Tic Tac Toe game. To start run: python -m main'''
    def __init__(self, board, active=True):
        self.board = board
        self.active = active
        

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
            move = input("Please, enter field ID for your next move.")
            try:
                move = int(move)
            except ValueError:
                print("Please enter ID between 1 and 9")
            else:
                if move >= 1 and move <= 9:
                    self.board[move] = 'X'
                    return move
                else:
                    print("ID must be a number between 1 and 9")

def main():
    bSize = [*range(11)]
    play = TicTac(bSize, True)
    while play.active == True:
        m1 = play.playRound()
        play.showBoard()

if __name__ == "__main__":main()