import unittest

from main import Board
from pieces import Pawn, Rook, Knight, Bishop, King, Queen

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test_blank_board_setup_black(self):
        """
        This tests that the black pieces on the board are setup correctly.
        """

        # Create a standard board.
        board = Board()

        # Check all the black pieces.
        self.assertIsInstance(board.get(0, 0), Rook)
        self.assertEqual(board.get(0, 0).player, "black")

        self.assertIsInstance(board.get(1, 0), Knight)
        self.assertEqual(board.get(1, 0).player, "black")

        self.assertIsInstance(board.get(2, 0), Bishop)
        self.assertEqual(board.get(2, 0).player, "black")

        self.assertIsInstance(board.get(3, 0), Queen)
        self.assertEqual(board.get(3, 0).player, "black")

        self.assertIsInstance(board.get(4, 0), King)
        self.assertEqual(board.get(4, 0).player, "black")

        self.assertIsInstance(board.get(5, 0), Bishop)
        self.assertEqual(board.get(5, 0).player, "black")

        self.assertIsInstance(board.get(6, 0), Knight)
        self.assertEqual(board.get(6, 0).player, "black")

        self.assertIsInstance(board.get(7, 0), Rook)
        self.assertEqual(board.get(7, 0).player, "black")

        for x in range(8):
            self.assertIsInstance(board.get(x, 1), Pawn)
            self.assertEqual(board.get(x, 1).player, "black")

    def test_blank_board_setup_white(self):
            """
            This tests that the white pieces on the board are setup correctly.
            """

            # Create a standard board.
            board = Board()

            # Check all the black pieces.
            self.assertIsInstance(board.get(0, 7), Rook)
            self.assertEqual(board.get(0, 7).player, "white")

            self.assertIsInstance(board.get(1, 7), Knight)
            self.assertEqual(board.get(1, 7).player, "white")

            self.assertIsInstance(board.get(2, 7), Bishop)
            self.assertEqual(board.get(2, 7).player, "white")

            self.assertIsInstance(board.get(3, 7), Queen)
            self.assertEqual(board.get(3, 7).player, "white")

            self.assertIsInstance(board.get(4, 7), King)
            self.assertEqual(board.get(4, 7).player, "white")

            self.assertIsInstance(board.get(5, 7), Bishop)
            self.assertEqual(board.get(5, 7).player, "white")

            self.assertIsInstance(board.get(6, 7), Knight)
            self.assertEqual(board.get(6, 7).player, "white")

            self.assertIsInstance(board.get(7, 7), Rook)
            self.assertEqual(board.get(7, 7).player, "white")

            for x in range(8):
                self.assertIsInstance(board.get(x, 6), Pawn)
                self.assertEqual(board.get(x, 6).player, "white")

    def test_valid_move_reversal(self):
        """
        This tests that a pieces valid moves successfully reverse based on their colour.
        """

        bp = Pawn("black")
        wp = Pawn("white")

        self.assertEqual(wp.moves()[6][7], 1)
        self.assertEqual(bp.moves()[8][7], 1)

if __name__ == '__main__':
    unittest.main()
