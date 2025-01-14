import Connect4Game as Game
import random


class RandomStrategy(Game.Connect4GameStrategy):
    """
    strategy class that selects moves randomly
    
    inherits from Connect4GameStrategy

    Methods
    -------

    strategy(game_safety_copy)
        determines next move using random strategy
    """

    def __init__(self, name="Daniel Batyrev"):
        """
        Initializes the RandomStrategy instance with a given name.
        
        Args:
            name (str): The name of the strategy or its creator. Defaults to "Daniel Batyrev".
        """
        self.name = name

    @classmethod
    def strategy(cls, game_safety_copy):
        """
        determines next move using random strategy
        
        Args:
            game_safety_copy (Connect4Game): safe copy of current game

        Returns:
            int: column index for next move, chosen randomly from valid moves
        """
        valid_moves = list()  # list to store all columns where move is valid
        for col in range(7):  # iterate over all columns in Connect4 board
            if game_safety_copy.is_valid_move(col):  # check if column is valid 
                valid_moves.append(col)  # add valid columns to list
        return random.choice(valid_moves)  # randomly select valid column for move

