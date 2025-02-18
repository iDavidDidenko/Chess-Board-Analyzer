class Pieces:
    
    def __init__(self, GUImanager, main_window, tk, image, os):
        self.GUImanager = GUImanager
        self.tk = tk
        self.image = image
        self.os = os
        self.__is_tile_selected = False


        self.pieces_frame = self.tk.Frame(main_window, width=200, height=400)
        self.pieces_frame.grid(row=0, column=2, padx=3, pady=10)

        #Pieces - btn Grid's
        self.white_pieces = tk.Frame(self.pieces_frame, width=200, height=200)
        self.white_pieces.grid(row=0, column=0, padx=0, pady=0)

        self.black_pieces = tk.Frame(self.pieces_frame, width=200, height=200)
        self.black_pieces.grid(row=1, column=0, padx=0, pady=0)

        self.__createPieces()
        
    def __createPieces(self):
        white_collection = ["Q", "N", "R", "B", "K", "P"]
        black_collection = ["q", "n", "r", "b", "k", "p"]
        self.__createPiecesOnGrid(self.white_pieces, white_collection)  
        self.__createPiecesOnGrid(self.black_pieces, black_collection)  

    def __createPiecesOnGrid(self, frame, pieace):
        base_dir = self.os.path.abspath(self.os.path.dirname(__file__))
        
        for i, piece in enumerate(pieace):
            j = (i // 3) + 1  # Row 
            z = i % 3          # Col 

            image_path = self.os.path.join(base_dir, "..", "Images", "White" if piece.isupper() else "Black", f"{piece}.png")
            img = self.tk.PhotoImage(file=image_path)

            tile = self.tk.Label(frame, image=img, bg="white", width=55, height=55, cursor="hand2")
            tile.image = img  # Prevent garbage collection
            tile.bind("<Button-1>", lambda event, p=piece: self.__handleOnClick(event, p))  # Avoid late binding
            tile.grid(row=j, column=z, padx=0, pady=0) 

    # TODO:
    # send also 'even' to extract image and pass to 
    def __handleOnClick(self, event, clicked_piece):

        if event.widget.cget("bg") == "white" and not self.__is_tile_selected:
            event.widget.config(bg="green")
            self.GUImanager.Board.setIsPieceSelected(True)
            self.GUImanager.Board.setHandlePiece(clicked_piece)
            self.__is_tile_selected = True

        elif event.widget.cget("bg") == "green":
            event.widget.config(bg="white")
            self.__is_tile_selected = False
            # self.GUImanager.Board.setIsPieceSelected(False)
            # self.GUImanager.Board.setHandlePiece(None)
