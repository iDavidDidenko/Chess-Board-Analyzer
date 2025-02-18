class Board:
    board_size = 8

    def __init__(self, GUImanager, main_window, tk):
        self.GUImanager = GUImanager
        self.tk = tk

        self.board = ['q' for _ in range(64)]

        self.__is_piece_selected = False
        self.__handle_piece = None

        self.board_frame = self.tk.Frame(main_window, width=500, height=500)
        self.board_frame.grid(row=0, column=0, padx=10, pady=5)

        self.__generateBoard()

    def __generateBoard(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                color = "white" if (row + col) % 2 == 0 else "#7d7c5b"
                tile = self.tk.Label(self.board_frame ,bg=color, width=11, height=5, cursor="hand2")
                tile.grid(row=row, column=col, padx=0, pady=0)
                tile.bind("<Button-1>", lambda event, r=row, c=col: self.__handleAddPiece(event, r, c)) 
                tile.bind("<Button-3>", lambda event, r=row, c=col: self.__handleRemovePiece(event, r, c))

    
    def setIsPieceSelected(self, is_white):
        self.__is_piece_selected = True if is_white else False

    def setHandlePiece(self, piece):
        self.__handle_piece = piece

    def __handleAddPiece(self, event, row, col):
        if self.__is_piece_selected:
            event.widget.config(text=self.__handle_piece)
            # write a formula to convert it from Row and Col (8x8) for 0 to 64 value
            index = self.__convert_tile_position(row, col)
            self.GUImanager.Controller.logic_board.set_piece(index, self.__handle_piece)

         
    def __handleRemovePiece(self, event, row, col):
        print("OK")
        index1 = self.__convert_tile_position(row, col)
        self.GUImanager.Controller.logic_board.remove_piece(index1)
        event.widget.config(text="") #should be with image TODO:

    def __convert_tile_position(self, row, col) -> int:
        return row * self.board_size + col

