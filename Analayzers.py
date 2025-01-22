import tkinter as tk
from PIL import Image, ImageTk

# Custom Python libs

# Define the size of the board
board_size = 8

# Create the main window
main_window = tk.Tk()
main_window.title("Analyzing Chess Games")
main_window.geometry("1024x720")
main_window.config(bg="skyblue")

##########################################################################

# create Board, menu and pieces frames using the grid layout
board_frame = tk.Frame(main_window, width=500, height=500)
board_frame.grid(row=0, column=0, padx=10, pady=5)

menu_frame = tk.Frame(main_window, width=120, height=400, bg="blue")
menu_frame.grid(row=0, column=1, padx=2, pady=10)

pieces_frame = tk.Frame(main_window, width=200, height=400, bg="green")
pieces_frame.grid(row=0, column=2, padx=3, pady=10)

##########################################################################


# Function's

# Create the chess pieces
def create_chess_pieces(frame):


# Create the chess board
def create_chess_board(frame):
    for row in range(board_size):
        for col in range(board_size):
            color = "white" if (row + col) % 2 == 0 else "#7d7c5b"
            tile = tk.Label(frame, bg=color, width=11, height=5, cursor="hand2")
            tile.grid(row=row, column=col, padx=0, pady=0)
            tile.bind("<Button-1>", lambda event, r=row, c=col: print(f"Tile clicked at row: {r}, column: {c}"))

##########################################################################

create_chess_board(board_frame)




main_window.mainloop()
