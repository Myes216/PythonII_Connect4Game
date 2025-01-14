from abc import (ABC, abstractmethod)

class Connect4GameStrategy(ABC):
    """
    an abstract base class for all strategies used by the ai
    all strategies will inherit from this class 

    Methods
    -------

    strategy(game_safety_copy)
        the abstract method to define the strategy for making a move
    """
    def __init__(self):
        """
        initializes Connect4GameStrategy 
        """
        ...

    @abstractmethod
    def strategy(self, game_safety_copy):
        """
        the abstract method to define the strategy for making a move
        
        Args:
            game_safety_copy: copy of the current game state which will prevent the original from being modified
        """
        ...


class Connect4Game:
    """
    class for the Connect 4 game logic
    handles the game board, move validation, player turns, and winner detection

    Methods
    -------

    is_valid_move(column)
        starts game with empty board, sets current player to 1, and sets the winner to None

    make_move(column)
        processes a player's move, updates the board, and switches current player
        if move results in a win, updates winner
    
    check_winner()
        checks if current player has won after placing a piece
    
    check_line()
        checks a line in a specified direction for four pieces in a row by current player
    """

    def __init__(self):
        """
        starts game with empty board, sets current player to 1, and sets winner to None
        """
        self.board = [[0] * 7 for _ in range(6)]  # 6 rows by 7 columns grid set to 0
        self.current_player = 1  # player 1 starts game
        self.winner = None  # no winner at the start

    def is_valid_move(self, column):
        """
        Checks if a move is valid for the given column.

        Args:
            column (int): column index

        Returns:
            bool: True if move is valid, False otherwise
        """
        if not (0 <= column < 7):  # Column must be between 0 and 6
            return False
        return self.board[0][column] == 0  # Top cell must be empty

    def make_move(self, column):
        """
        processes a player's move, updates the board, and switches current player
        if move results in a win, updates winner

        Args:
            column (int): column index where player places their piece
        """
        if not self.is_valid_move(column) or self.winner is not None:
            return  # Invalid move or game already has a winner

        # Find the lowest empty row in the specified column
        for row in range(5, -1, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = self.current_player               
                if self.check_winner(row, column): # checks for win
                    self.winner = self.current_player  # declare current player winner
                else:
                    self.current_player = 3 - self.current_player  # switch toother player
                return

    def check_winner(self, row, col):
        """
        checks if current player has won after placing a piece

        Args:
            row (int): row index 
            col (int): column index 

        Returns:
            bool: True if current player has won, False otherwise
        """
        # list of directions, horizontal, vertical, diagonal and reverse diagonal
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        results = [self.check_line(row, col, dr, dc) for dr, dc in directions]# checks directions for winning line
        return any(results)

    def check_line(self, row, col, dr, dc):
        """
        checks a line in a specified direction for four pieces in a row by current player

        Args:
            row (int): Starting row index
            col (int): Starting column index
            dr (int): Row direction increment
            dc (int): Column direction increment 
        Returns:
            bool: True if there are four pieces in a row by current player, False otherwise
        """
        count = 0  # count of pieces in a row
        row = row - dr * 3  # adjust start position to check backward
        col = col - dc * 3

        # check 7 positions in the direction
        for _ in range(7):
            # check if current position is valid and belongs to the current player
            if 0 <= row < 6 and 0 <= col < 7 and self.board[row][col] == self.current_player:
                count += 1  # increment the count for a valid piece
                if count == 4:  # win condition met
                    return True
            else:
                count = 0  # reset count if the sequence is broken
            row += dr  # move to next row in direction
            col += dc  # move to next column in direction

        return False  # if no winning line found
 
