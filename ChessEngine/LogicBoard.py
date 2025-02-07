import chess

class LogicBoard:

    def __init__(self):
        # TODO
        self.board = chess.Board.empty() 

    def set_empty_board(self):
        self.board = chess.Board.empty()    

    def set_standard_board(self):
        self.board = chess.Board()

    def set_piece(self, tile: int, piece: str):
        if not self.board:
            raise ValueError("Board is not initialized.")
        
        try:
            chess_piece = chess.Piece.from_symbol(piece)
            self.board.set_piece_at(tile, chess_piece)
        except ValueError as e:
            raise ValueError(f"Invalid piece symbol '{piece}': {e}")

    def set_turn(self, is_white: bool): 
        if not isinstance(is_white, bool):
            raise TypeError("LogicBoard - is_white must be a boolean.")
        self.board.turn = is_white

    def get_board(self) -> str:
        if self.board is None:
            raise ValueError("LogicBoard - Board is not initialized...")
        return self.board.fen()  
            