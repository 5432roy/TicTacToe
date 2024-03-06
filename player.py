# author: Shang-Yu Chan
# date: 10/18/2022

import random
import time

class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
            self.valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']

      # return player's sign
      def get_sign(self):
            return self.sign

      # return player's name
      def get_name(self):
            return self.name

      # let the player select the cell on board
      def choose(self, board):
            while True:
                  # prompt the user to choose a cell
                  cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ').upper()
                  
                  # print a message that the input is wrong and rewrite the prompt
                  if cell not in self.valid_choices or not board.isempty(cell) :
                        print('You did not choose correctly')
                        continue
                  # if the user enters a valid string and the cell on the board is empty, update the board
                  # use the methods board.isempty(cell), and board.set(cell, sign)
                  board.set(cell, self.sign)
                  break

# Simple Robot that select the cell at random
class AI(Player):
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X

            # robot needs to know who is the opponent to do certain calculation
            self.opponent = 'X' if sign == 'O' else 'O'
            self.valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
      
      # select the cell
      def choose(self, board):
            print(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ', end = '')
            while True:
                  # select valid cells at random
                  cell = random.choice(self.valid_choices)
                  if board.isempty(cell):
                        board.set(cell, self.sign)
                        print(cell)
                        break
            time.sleep(1)

# An algorithm that plays the game base on heuristic approach. The AI never loses the game and can win some games depends on oppoenet's move
# Perfect game approach base on https://en.wikipedia.org/wiki/Tic-tac-toe.
class SmartAI(AI):
      def choose(self, board):
            print(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ', end = '')
            time.sleep(1)
            # check win condition
            for cell in self.valid_choices:
                  if board.isempty(cell):
                        board.set(cell, self.sign)
                        if board.isdone() and board.get_winner() == self.sign:
                              print(cell)
                              return
                        board.set(cell, ' ')
            # check lose condition
            for cell in self.valid_choices:
                  if board.isempty(cell):
                        board.set(cell, self.opponent)
                        if board.isdone() and board.get_winner() == self.opponent:
                              board.set(cell, self.sign)
                              print(cell)
                              return
                        board.set(cell, ' ')
            # check fork condition
            for cell in self.valid_choices:
                  if board.isempty(cell):
                        board.set(cell, self.sign)
                        if self.can_win(board, self.sign) > 1:
                              print(cell)
                              return
                        board.set(cell, ' ')
            # check blocking fork conidition
            for cell in self.valid_choices:
                  if board.isempty(cell):
                        board.set(cell, self.opponent)
                        if self.can_win(board, self.opponent) > 1:
                              board.set(cell, self.sign)
                              print(cell)
                              return
                        board.set(cell, ' ')
            
            # check if center is empty
            if board.isempty('B2'):
                  board.set('B2', self.sign)
                  print(cell)
                  return
            # check opposite corner
            corner = {0:8, 8:0, 2:6, 6:2}
            for key in corner.keys():
                  if board.board[key] == self.opponent and board.isempty(self.valid_choices[corner[key]]):
                        board.set(self.valid_choices[corner[key]], self.sign)
                        print(cell)
                        return
            # check corner
            for key in corner:
                  if board.isempty(self.valid_choices[key]):
                        board.set(self.valid_choices[key], self.sign)
                        print(cell)
                        return
            # check side:
            for i in range(1, 8, 2):
                  if board.isempty(self.valid_choices[i]):
                        board.set(self.valid_choices[key], self.sign)
                        print(cell)
                        return

            # if the program runs to here something went wrong badly
            print("****Program Error****")

      # a helper function that helps calculate how many ways can finish the game in one move
      def can_win(self, board, sign):
            res = 0
            for cell in self.valid_choices:
                  if board.isempty(cell):
                        board.set(cell, sign)
                        res += 1 if board.isdone() and board.get_winner() == sign else 0
                        board.set(cell, ' ')
            return res

# An AI that select next move base on the calculation of all possibility and return the move of the best expectation value
class MiniMax(AI):
      def choose(self, board):
            # default value for the expecatation
            # there is no Integer.MIN_VALUE in python like java does
            res = -1000
            move = -1

            # calculate the expectation value of all move
            for i in range(9):
                  cell = self.valid_choices[i]
                  if board.isempty(cell):
                        board.set(cell, self.sign)
                        cur = self.backtracking(board, 0, False)
                        board.set(cell, ' ')
                        # store the current best move
                        if cur > res:
                              res = cur
                              move = i
            # prompt to the terminal to help understand the process of the game
            print(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]: {self.valid_choices[move]}')
            
            #
            time.sleep(1)
            
            # make the final decision with the best value
            board.set(self.valid_choices[move], self.sign)

      # the AI calculation is a straightforward process of Backtracking
      # using depth the help distinguish the more efficient move that lead to the same result
      def backtracking(self, board, depth, myTurn):
            # base case
            if board.isdone():
                  if board.get_winner() == "":
                        return 0
                  return 10 - depth if board.get_winner() == self.sign else depth - 10
                  
            res = 0
            if myTurn:
                  res = -1000
                  for i in range(9):
                        cell = self.valid_choices[i]
                        if board.isempty(cell):
                              board.set(cell, self.sign)
                              res = max(res, self.backtracking(board, depth + 1, not myTurn))
                              board.set(cell, ' ')
                  return res
            else:
                  res = 1000
                  for i in range(9):
                        cell = self.valid_choices[i]
                        if board.isempty(cell):
                              board.set(cell, self.opponent)
                              res = min(res, self.backtracking(board, depth + 1, not myTurn))
                              board.set(cell, ' ')
                  return res
