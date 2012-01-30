from ipdb import set_trace
from pieces import Pawn, Rook, Knight, Bishop, King, Queen

class Board(object):
    """
    This is the board.
    """

    def __init__(self, state=False):
        """
        Initialises the board with a starting set of pieces, or to an optional state, as defined by a JSON string.
        """

        # If we have a state, then use it here.
        if state:
            pass

        # Initialise an empty board.
        else:
            self.state = []
            for y in range(8):
                row = []
                for x in range(8):
                    row.append(False)
                self.state.append(row)

        # Add the black pieces to the board.
        self.put(Rook("black"), 0, 0)
        self.put(Knight("black"), 1, 0)
        self.put(Bishop("black"), 2, 0)
        self.put(Queen("black"), 3, 0)
        self.put(King("black"), 4, 0)
        self.put(Bishop("black"), 5, 0)
        self.put(Knight("black"), 6, 0)
        self.put(Rook("black"), 7, 0)

        # Now the black pawns
        for bp in range(8):
            self.put(Pawn("black"), bp, 1)

        # Add the white pieces to the board.
        self.put(Rook("white"), 0, 7)
        self.put(Knight("white"), 1, 7)
        self.put(Bishop("white"), 2, 7)
        self.put(Queen("white"), 3, 7)
        self.put(King("white"), 4, 7)
        self.put(Bishop("white"), 5, 7)
        self.put(Knight("white"), 6, 7)
        self.put(Rook("white"), 7, 7)

        # Now the white pawns
        for wp in range(8):
            self.put(Pawn("white"), wp, 6)

    def get(self, x, y):
        """
        This returns a piece on the board.
        """

        return self.state[x][y]

    def put(self, piece, x, y):
        """
        This places a piece on the board.
        """

        self.state[x][y] = piece

    def delete(self, x, y):
        """
        This removes a piece from the board.
        """

        self.state[x][y] = None

    def move(self, x1, y1, x2, y2):
        """
        This moves a piece on the board. This is where the magic happens.
        """

        # First, check we are trying to move a valid piece.
        if not self.get(x1, y1):
            return False

        self.put(self.get(x1, y1), x2, y2)
        self.delete(x1, y1)

    def render(self):
        """
        This renders the board.
        """

        for y in range(8):
            row = ""
            for x in range(8):
                piece = self.get(x, y)
                if piece:
                    row += str(piece)
                else:
                    row += " "
            print row

if __name__ == '__main__':

    # Create our board.
    board = Board()

    # Start a ghetto-repl.
    set_trace()
