# author: Shang-Yu Chan
# date: 10/18/2022
# file: tictac.py a Python program that implements a tic-tac-toe game
# input: user responses (strings)
# output: 1. interactive text messages and a tic-tac-toe board
#         2. the result of different AIs playing tic-tac-toe

from board import Board
from player import *

# the Tic Tac Toe game class
class TicTacToe:
    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        
    # let user select the player type by terminal input
    def player_selection(self, player, sign):
        player_type = {
            '1': Player("Player", sign),
            '2': AI("Stupid Computer", sign),
            '3': SmartAI("Unbeatable AI", sign),
            '4': MiniMax("MiniMax AI", sign)
        }
        
        user_input = input(f"Who is the player for '{sign}'?\n'1' for user, '2' for Stupid Computer, '3' for Unbeatable AI, '4' for MiniMax_AI \n")
        while user_input not in player_type :
            player = input("Please select the correct player type\n")
        if player == 1 :
            self.player1 = player = player_type[user_input]
        else :
            self.player2 = player = player_type[user_input]

    # the main functin that execute the game
    def new_game(self):
        print("Welcome to TIC-TAC-TOE Game!")
        while True:
            board = Board()
            self.player_selection(1, "X")
            self.player_selection(2, "O")
            print(type(self.player1))
            turn = True
            while True:
                board.show()
                if turn:
                    self.player1.choose(board)
                    turn = False
                else:
                    self.player2.choose(board)
                    turn = True
                if board.isdone():
                    break
            board.show()
            if board.get_winner() == self.player1.get_sign():
                print(f"{self.player1.get_name()} is a winner!")
            elif board.get_winner() == self.player2.get_sign():
                print(f"{self.player2.get_name()} is a winner!")
            else:
                print("It is a tie!")
            ans = input("Would you like to play again? [Y/N]\n").upper()
            if (ans != "Y"):
                break
        print("Goodbye!")

if __name__ == "__main__":
    tictactoe = TicTacToe()
    tictactoe.new_game()