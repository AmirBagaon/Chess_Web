from stockfish import Stockfish

class DataHanlder():
    def __init__(self, data) -> None:
        self._data = data
        print()
        path = r"./main/engine/c_engine.exe"
        self.stockfish = Stockfish(path)
    
    def handle(self):
        return self.get_best_move()

    def get_best_move(self):
        self.stockfish.set_fen_position(self._data)
        return self.stockfish.get_best_move()


# stockfish.set_fen_position("rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2")
# x = stockfish.get_best_move()
# print(x)