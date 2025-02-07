from stockfish import Stockfish
import os

class StockfishAnalyzer:

    def __init__(self):
        self.stockfish_path = os.path.abspath(os.path.join("ChessEngine", "stockfish-windows-x86-64-avx2.exe"))

        try:
            self.stockfish = Stockfish(path=self.stockfish_path)
        except Exception as e:
            raise RuntimeError(f"In StockfishAnalyzer - Failed to initialize Stockfish: {e}")
                
    def set_turn(self, is_white: bool):
        self.stockfish.set_turn_perspective(is_white)

    def set_fen(self, fen: str):
        self.stockfish.set_fen_position(fen)

    def get_best_move(self) -> str:
        return self.stockfish.get_best_move()
