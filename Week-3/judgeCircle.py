"""
657. There is a robot starting at position (0, 0), the origin, on a 2D plane.
Given a sequence of its moves, judge if this robot ends up at (0, 0)
after it completes its moves.

The move sequence is represented by a string, and the character moves[i] represents
its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the
robot returns to the origin after it finishes all of its moves, return true.
Otherwise, return false.

"""

class Solution:
    def judgeCircle(self, moves):
        d = {'L':0 ,'R':0,'U':0,'D':0}

        for char in moves:
            d[char] = d.get(char,0) +1
        if d['L'] == d['R'] and d['U'] == d['D']:
            return True
        else:
            return False


def main():
    sol = Solution()
    print(sol.judgeCircle("LR"))

if __name__ == "__main__":
    main()