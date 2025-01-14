import tkinter as tk
from tkinter import messagebox
import Connect4Game as game
import DanielBatyrevAI as DanielAI
import copy

# strategies for AI players
random_choice = DanielAI.RandomStrategy()  # random move strategy
yosef_choice = YosefAI.AI_strategy()  # Yosef's AI strategy
shmuli_choice = ShmulyAI.NotRandomStrategy()  # Shmuli's AI strategy

class Connect4GUI:
    """
    GUI for Connect 4

    Methods
    -------

    make_move(column)
        handles logic for player move and AI response

    draw_board()
        draws Connect 4 board 
    """

    def __init__(self, master):
        """
        initializes Connect4GUI

        Args:
            master (tk.Tk): The root Tkinter window instance.
        """
        self.master = master
        self.master.title("Connect 4")  # Set the title of the game window
        self.game = game.Connect4Game()  # Initialize a new Connect 4 game instance

        # Create buttons for column selection
        self.buttons = []
        for col in range(7):
            button = tk.Button(
                master, 
                text=str(col + 1),  # Button text represents the column number
                command=lambda c=col: self.make_move(c)  # Attach move-making function
            )
            button.grid(row=0, column=col)  # Place buttons in the first row
            self.buttons.append(button)

        # Create a canvas to visualize the game board
        self.canvas = tk.Canvas(master, width=7 * 60, height=6 * 60)  # 7 columns, 6 rows
        self.canvas.grid(row=1, column=0, columnspan=7)  # Span canvas across all columns
        self.draw_board()  # Draw the initial empty board

    def make_move(self, column):
        """
        handles logic for player move and AI response
        
        Args:
            column (int): column index for player move
        """
        self.game.make_move(column)  # make player move
        self.draw_board()  # update board 

        # check if player won
        if self.game.winner is not None:
            winner_text = f"Player {self.game.winner} wins!"  # display winner
            messagebox.showinfo("Game Over", winner_text)  # show game-over message
            self.master.destroy()  # close game window
        else:
            # make move for AI
            game_copy = copy.deepcopy(self.game)  # create copy of game 
            self.game.make_move(shmuli_choice.strategy(game_copy))  # AI makes move
            self.draw_board()  # update  board 

            # check if AI won
            if self.game.winner is not None:
                winner_text = f"Player {self.game.winner} wins!"  # display winner
                messagebox.showinfo("Game Over", winner_text)  # show game-over message
                self.master.destroy()  # lose game window

    def draw_board(self):
        """
        draws Connect 4 board 
        """
        self.canvas.delete("all")  # clear the canvas

        # draw board and pieces
        for row in range(6):  # iterate over all rows
            for col in range(7):  # iterate over all columns
                x0, y0 = col * 60, row * 60  # top-left corner of the cell
                x1, y1 = x0 + 60, y0 + 60  # bottom-right corner of the cell
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="white") 

                # draw player pieces
                if self.game.board[row][col] == 1:  # player 1's piece (red)
                    self.canvas.create_oval(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill="red", outline="red")
                elif self.game.board[row][col] == 2:  # player 2's piece (yellow)
                    self.canvas.create_oval(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill="yellow", outline="yellow")

        # enable or disable buttons 
        for col in range(7):
            if self.game.board[0][col] == 0:  # column not full
                self.buttons[col]["state"] = tk.NORMAL  # enable button
            else:  # column full
                self.buttons[col]["state"] = tk.DISABLED  # disable button


if __name__ == "__main__":
    """
    entry for program, creates main Tkinter window and starts game
    """
    root = tk.Tk()  # create root window
    app = Connect4GUI(root)  # initialize game GUI
    root.mainloop()  # run Tkinter event loop

