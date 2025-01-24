import tkinter as tk
from .Board import Board
from .Menu import Menu
from .Pieces import Pieace

class GUImanager:

    def __init__(self, title, size):
        self.main_window = tk.Tk()
        self.main_window.title(title)
        self.main_window.geometry(size)
        self.main_window.config(bg="skyblue")

        self.Board = Board(self, self.main_window, tk)
        self.Menu = Menu(self, self.main_window, tk)
        self.Pieces = Pieace(self, self.main_window, tk)

        

    def startWindow(self):
        self.main_window.mainloop()

    #     # Pieces - btn Grid's
    #     self.white_pieces = tk.Frame(self.pieces_frame, width=200, height=200, bg="white")
    #     self.white_pieces.grid(row=0, column=0, padx=0, pady=0)

    #     self.black_pieces = tk.Frame(self.pieces_frame, width=200, height=200, bg="black")
    #     self.black_pieces.grid(row=1, column=0, padx=0, pady=0)

    


    # def __createPieces(self):
    #     white_collection = ["Q", "N", "R", "B", "K", "P"]
    #     black_collection = ["q", "n", "r", "b", "k", "p"]
    #     self.__createPiecesOnGrid(self.white_pieces, white_collection)  
    #     self.__createPiecesOnGrid(self.black_pieces, black_collection)  

    # def __createPiecesOnGrid(self, frame, pieace):
    #     pieces = ["Q", "N", "R", "B", "K", "P"]
    #     i = 0
    #     j = 0
    #     for i, piece in enumerate(pieace):
    #         if i % 3 == 0:
    #             j += 1
    #             z = 0
    #         tile = tk.Label(frame, text=piece, bg="white", width=9, height=4, cursor="hand2")
    #         tile.bind("<Button-1>", lambda event, piece=piece: self.__handleClickedPiece(event, piece))            
    #         tile.grid(row=j, column=z, padx=0, pady=0)  
    #         z += 1  

    # def __handleClickedPiece(self, event, piece):
    #     if self.current_piece is None:
    #         self.current_piece = piece
    #         event.widget.config(bg="red")
    #         print(self.current_piece)

    # def __createMenu(self):
    #         self.btn_analiyze = tk.Button(self.menu_frame, text="Analyze", width=10, height=2, bg="white")
    #         self.btn_analiyze.grid(row=0, column=0, padx=0, pady=0)

    #         btn_reset = tk.Button(self.reset_btn, text="Reset", width=10, height=2, bg="orange")
    #         btn_reset.grid(row=1, column=0, padx=0, pady=0)
