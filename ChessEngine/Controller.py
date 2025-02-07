from .LogicBoard import LogicBoard
from .StockfishAnalyzer import StockfishAnalyzer

class Controller:

    def __init__(self):
        self.board = LogicBoard() # by default initial empty board TODO
        self.stockfish = StockfishAnalyzer()



    def set_white_turn(self):
        self.board.turn = True
        print(self.board.turn)

    def set_black_turn(self):
        self.board.turn = False  
        print(self.board.turn)

    # TODO 
    def analayzer(self, board):
        print(board)
        self.board.board.fen(board)