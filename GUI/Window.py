
import tkinter as tk

class Window:
    board_size = 8

    def __init__(self, title, size):
        self.main_window = tk.Tk()
        self.main_window.title(title)
        self.main_window.geometry(size)
        self.main_window.config(bg="skyblue")

    def createGrids(self):
        self.board_frame = tk.Frame(self.main_window, width=500, height=500)
        self.board_frame.grid(row=0, column=0, padx=10, pady=5)

        self.menu_frame = tk.Frame(self.main_window, width=120, height=400, bg="blue")
        self.menu_frame.grid(row=0, column=1, padx=2, pady=10)

        self.pieces_frame = tk.Frame(self.main_window, width=200, height=400, bg="green")
        self.pieces_frame.grid(row=0, column=2, padx=3, pady=10)

        # Menu - btn Grid's
        self.analiyze_btn = tk.Frame(self.menu_frame, width=100, height=50, bg="red")
        self.analiyze_btn.grid(row=0, column=0, padx=0, pady=0)

        self.reset_btn = tk.Frame(self.menu_frame, width=100, height=50, bg="yellow")
        self.reset_btn.grid(row=1, column=0, padx=0, pady=0)

        # Pieces - drag and drop Grid's
        self.white_pieces = tk.Frame(self.pieces_frame, width=200, height=200, bg="white")
        self.white_pieces.grid(row=0, column=0, padx=0, pady=0)

        self.black_pieces = tk.Frame(self.pieces_frame, width=200, height=200, bg="black")
        self.black_pieces.grid(row=1, column=0, padx=0, pady=0)

    

    def createBoard(self):
        self.__createBoard()
        self.__createMenu()

    def __createBoard(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                color = "white" if (row + col) % 2 == 0 else "#7d7c5b"
                tile = tk.Label(self.board_frame, text ="QUEEN" ,bg=color, width=11, height=5, cursor="hand2")
                tile.grid(row=row, column=col, padx=0, pady=0)
            # tile.bind("<Button-1>", lambda event, r=row, c=col: print(tile.cget("text") == E_Pieces.QUEEN.name))

    def __createMenu(self):
            btn_analiyze = tk.Button(self.analiyze_btn, text="Analyze", width=10, height=2, bg="white")
            btn_analiyze.grid(row=0, column=0, padx=0, pady=0)

            btn_reset = tk.Button(self.reset_btn, text="Reset", width=10, height=2, bg="orange")
            btn_reset.grid(row=1, column=0, padx=0, pady=0)


    def startWindow(self):
        self.main_window.mainloop()