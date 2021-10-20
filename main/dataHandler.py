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
        position = str(self._data).strip()
        if " " in position:
          self.stockfish.set_fen_position(position)
          returnValue = self.stockfish.get_best_move()
          return {'message': returnValue}
        else:
          white_turn = position + " w KQkq - 0 1"
          self.stockfish.set_fen_position(white_turn)
          white_best_move = self.stockfish.get_best_move()
          black_turn = position + " b KQkq - 0 1"
          self.stockfish.set_fen_position(black_turn)
          black_best_move = self.stockfish.get_best_move()

          #Now if the board is from black perspective, it will predict it in the opposite way,
          #So need to reverse it
          position = position[::-1]
          r_white_turn = position + " w KQkq - 0 1"
          self.stockfish.set_fen_position(r_white_turn)
          r_white_best_move = self.stockfish.get_best_move()
          r_black_turn = position + " b KQkq - 0 1"
          self.stockfish.set_fen_position(r_black_turn)
          r_black_best_move = self.stockfish.get_best_move()
          return {'white': white_best_move, 'black': black_best_move,
          'reverse_white' : r_white_best_move, 'reverse_black' : r_black_best_move,
          'message': ""}
          

        # return self.stockfish.get_best_move_time(2000)
        # return self.stockfish.get_best_move()

    @staticmethod
    def getOneVsOne():
        return """
        var whiteSquareGrey = '#a9a9a9'
var blackSquareGrey = '#696969'

function removeGreySquares () {
  $('#chess_board .square-55d63').css('background', '')
}

function greySquare (square) {
  var $square = $('#chess_board .square-' + square)

  var background = whiteSquareGrey
  if ($square.hasClass('black-3c85d')) {
    background = blackSquareGrey
  }

  $square.css('background', background)
}

function onDragStart (source, piece) {
  // do not pick up pieces if the game is over
  if (game.game_over()) return false

  // or if it's not that side's turn
  if ((game.turn() === 'w' && piece.search(/^b/) !== -1) ||
      (game.turn() === 'b' && piece.search(/^w/) !== -1)) {
    return false
  }
}

function onDrop (source, target) {
  removeGreySquares()

  // see if the move is legal
  var move = game.move({
    from: source,
    to: target,
    promotion: 'q' // NOTE: always promote to a queen for example simplicity
  })

  // illegal move
  if (move === null) return 'snapback'
}

function onMouseoverSquare (square, piece) {
  // get list of possible moves for this square
  var moves = game.moves({
    square: square,
    verbose: true
  })

  // exit if there are no moves available for this square
  if (moves.length === 0) return

  // highlight the square they moused over
  greySquare(square)

  // highlight the possible squares for this piece
  for (var i = 0; i < moves.length; i++) {
    greySquare(moves[i].to)
  }
}

function onMouseoutSquare (square, piece) {
  removeGreySquares()
}

function onSnapEnd () {
  board.position(game.fen())
}

var config = {
  draggable: true,
  position: 'start',
  onDragStart: onDragStart,
  onDrop: onDrop,
  onMouseoutSquare: onMouseoutSquare,
  onMouseoverSquare: onMouseoverSquare,
  onSnapEnd: onSnapEnd
}
        """


    @staticmethod
    def getRandomPlay():
        return """
        function makeRandomMove () {
  var possibleMoves = game.moves()

  // exit if the game is over
  if (game.game_over()) return

  var randomIdx = Math.floor(Math.random() * possibleMoves.length)
  game.move(possibleMoves[randomIdx])
  board.position(game.fen())

  window.setTimeout(makeRandomMove, 5)
}
window.setTimeout(makeRandomMove, 500)
var config = {
  position: 'start',
}
        """
    @staticmethod
    def getVsAI():
        return """
function makeMove() {
    sendForm()
    console.log("$$$$$$$$$$$$")
    updateStatus()
        console.log("$$$$$$$$$$$$")
    if (game.game_over()) {
    return
  }

//   window.setTimeout(makeMove, 500)
}

function onDragStart (source, piece, position, orientation) {
  // do not pick up pieces if the game is over
  if (game.game_over()) return false

  // only pick up pieces for White
  if (piece.search(/^b/) !== -1) return false
}

function onDrop (source, target) {
  // see if the move is legal
  var move = game.move({
    from: source,
    to: target,
    promotion: 'q' // NOTE: always promote to a queen for example simplicity
  })

  // illegal move
  if (move === null) return 'snapback'
    console.log("!!!!!!!!")
  updateStatus()
      console.log("!!!!!!!!")
  // make random legal move for black
  window.setTimeout(makeMove, 250)
}

// update the board position after the piece snap
// for castling, en passant, pawn promotion
function onSnapEnd () {
  board.position(game.fen())
}

var config = {
  draggable: true,
  position: 'start',
  onDragStart: onDragStart,
  onDrop: onDrop,
  onSnapEnd: onSnapEnd
}
function startGame() {

}
    """

# stockfish.set_fen_position("rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2")
# x = stockfish.get_best_move()
# print(x)