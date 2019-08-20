"""
794. A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach
this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " "
character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.

"""

import unittest

class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        counts, lines = [0,0] , [0,0]

        for i,char in enumerate(("O","X")):
            for j,row in enumerate(board):
                if row == char*3:
                    lines[i] += 1
                if board[0][j] == board[1][j] == board[2][j] == char:
                    lines[i]  += 1

                for c in row:
                    if c == char :
                        counts[i] += 1

            if board[0][0] == board[1][1] == board[2][2] == char :
                lines[i] += 1
            if board[2][0] == board[1][1] == board[0][2] == char:
                lines[i] += 1

        if lines[0] and lines[1]:
            return False
        if lines[0] and counts[0] != counts[1]:
            return False
        if lines[1] and counts[1] != counts[0] +1:
            return False
        if counts[1] - counts[0] > 1 or counts[1] - counts[0] < 0:
            return False
        return  True

class Test_Program(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        result = self.sol.validTicTacToe(board = ["O  ", "   ", "   "])
        self.assertEquals(result,False)

    def test_case_2(self):
        result = self.sol.validTicTacToe(board = ["XOX", " X ", "   "])
        self.assertEquals(result,False)

    def test_case_3(self):
        result = self.sol.validTicTacToe(board = ["XXX", "   ", "OOO"])
        self.assertEquals(result,False)

    def test_case_4(self):
        result = self.sol.validTicTacToe(board = ["XOX", "O O", "XOX"])
        self.assertEquals(result,True)

if __name__ == "__main__":
    unittest.main()

