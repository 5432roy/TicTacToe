# author: Shang-Yu Chan
# date: 10/18/2022

class Board:
      def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size**2)
            self.valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            # the winner's sign O or X
            self.winner = ""

      # return the size of the board
      def get_size(self):
            return self.size

      # return the winner of the game
      def get_winner(self):
            return self.winner


      # mark the cell on the board with the sign X or O or Empty
      def set(self, cell, sign):
            # turn the string input into index for board
            index = self.valid_choices.index(cell)
            self.board[index] = sign

            # everytime we set the board, we should clear the winner as well
            self.winner = ""
      
      # return if a certain cell is empty or not
      def isempty(self, cell):
            return self.board[self.valid_choices.index(cell)] == self.sign

      # return if the game is ended
      def isdone(self):

            # Diagonal
            if self.board[4] != self.sign:
                  if len(set([sign for sign in self.board[::4]])) == 1 or len(set([sign for sign in self.board[2:7][::2]])) == 1:
                        self.winner = self.board[4]
                        return True

            for i in range(self.size):
                  # Horizontal
                  cur = set(self.board[i * self.size : i * self.size + 3])
                  if len(cur) == 1 and self.sign not in cur:
                        self.winner = cur.pop()
                        return True
                  # Vertical
                  cur = set(self.board[i::3])
                  if len(cur) == 1 and self.sign not in cur:
                        self.winner = cur.pop()
                        return True

            # board is full but no one wins
            return not any(cell == ' ' for cell in self.board)

      # print out the board
      def show(self):
            print('   A   B   C') 
            print(' +---+---+---+')
            for i in range(3):
                  print('{}| {} | {} | {} |'.format(i + 1, self.board[0 + i * 3], self.board[1 + i * 3], self.board[2 + i * 3]))
                  print(' +---+---+---+')
               