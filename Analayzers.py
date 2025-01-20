import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
m = tk.Tk()
m.title("Analyzing Chess Games")

# Define the size of the board
board_size = 8

# Create a frame to hold the tiles
frame = tk.Frame(m)
frame.pack(side=tk.LEFT, padx=int(m.winfo_screenwidth() * 0.2), pady=10, expand=True, fill=tk.BOTH)

# Load images for list items
piece_images = {}
for piece in ['wp', 'bp', 'wr', 'br', 'wn', 'bn', 'wb', 'bb', 'wq', 'bq', 'wk', 'bk']:
    image = Image.open(f'Images/{piece}.png')
    image = image.resize((64, 64), Image.ANTIALIAS)
    piece_images[piece] = ImageTk.PhotoImage(image)

# Function to handle tile click
def on_tile_click(event, row, col):
    print(f"Tile clicked at row: {row}, column: {col}")

# Function to create the chess board
def create_chess_board(frame):
    for row in range(board_size):
        for col in range(board_size):
            color = "white" if (row + col) % 2 == 0 else "#7d7c5b"
            tile = tk.Label(frame, bg=color, width=8, height=4)
            tile.grid(row=row, column=col, padx=2, pady=2)
            tile.bind("<Button-1>", lambda event, r=row, c=col: on_tile_click(event, r, c))
            tile.bind("<ButtonRelease-1>", on_drop)
            tile.row = row
            tile.col = col

# Create the chess board
create_chess_board(frame)

# Create a frame to take up the remaining 30% of the space
right_frame = tk.Frame(m, width=int(m.winfo_screenwidth() * 0.3))
right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# Create two lists in the right frame
list1 = tk.Listbox(right_frame)
list2 = tk.Listbox(right_frame)

# Pack the lists into the right frame
list1.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
list2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Add some sample items to the lists
for piece in piece_images.keys():
    list1.insert(tk.END, piece)
    list2.insert(tk.END, piece)

# Function to handle list item click
def on_list_item_click(event):
    widget = event.widget
    selection = widget.curselection()
    if selection:
        index = selection[0]
        value = widget.get(index)
        print(f"List item clicked: {value}")

# Bind the click event to the list items
list1.bind('<<ListboxSelect>>', on_list_item_click)
list2.bind('<<ListboxSelect>>', on_list_item_click)

# Variables to store drag-and-drop state
drag_data = {"item": None, "index": None, "widget": None}

# Function to handle the start of a drag
def on_drag_start(event):
    widget = event.widget
    index = widget.nearest(event.y)
    drag_data["item"] = widget.get(index)
    drag_data["index"] = index
    drag_data["widget"] = widget

# Function to handle the end of a drag
def on_drop(event):
    widget = event.widget
    if drag_data["item"]:
        piece_image = piece_images[drag_data["item"]]
        widget.config(image=piece_image)
        widget.image = piece_image
        drag_data["item"] = None
        drag_data["index"] = None
        drag_data["widget"] = None

# Bind the drag-and-drop events to the listboxes
list1.bind("<ButtonPress-1>", on_drag_start)
list2.bind("<ButtonPress-1>", on_drag_start)

# Start the main loop
m.mainloop()