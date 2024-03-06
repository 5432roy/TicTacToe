# TicTacToe
Create a Tic-Tac-Toe game using python, the process of the game will be print to the terminal.

## Usage
- Start the program: `python tictac.py`
- Select the player type: `'1' for user, '2' for Stupid Computer, '3' for Unbeatable AI, '4' for MiniMax_AI`
- Select the move: Type in the desired location with the format `[A-C][1-3]`, case ignored

## Description for Different type of Machine:
- Stupid Computer: which select the valid grid by random.
- Unbeatable AI: An algorithm that plays the game base on heuristic approach. The AI never loses the game and can win some games depends on oppoenet's move. Please refer to Perfect game approach base on https://en.wikipedia.org/wiki/Tic-tac-toe.
- MiniMax AI: Select next move base on the calculation of all possibility and return the move of the best expectation value. Using decision tree pruning to help reduce the runtime.