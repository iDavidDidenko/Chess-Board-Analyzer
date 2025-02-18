from .LogicBoard import LogicBoard
from .StockfishAnalyzer import StockfishAnalyzer

class Controller:

    def __init__(self):
        self.__stockfish = StockfishAnalyzer()

        self.logic_board = LogicBoard() # by default initial empty board TODO

    
    def set_white_turn(self):
        self.logic_board.set_turn(True)
        print(f"Turn: {self.logic_board.get_turn()}")

    def set_black_turn(self):
        self.logic_board.set_turn(False)  
        print(f"Turn: {self.logic_board.get_turn()}")

    # TODO 
    def analayzer(self):
        self.__stockfish.set_fen(self.logic_board.get_fen())
        print(f"Best move is: {self.__stockfish.get_best_move()}")
        