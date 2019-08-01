"""
688. On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to
make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0),
and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two
squares in a cardinal direction, then one square in an orthogonal direction.
"""


class Solution:
    def knightProbability(self, N, K, r, c):

        prev_dp = [[0 for i in range(N)] for j in range(N)]
        prev_dp[r][c] = 1
        directions = [(1, 2), (1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
        for k in range(K):
            new_dp = [[0 for i in range(N)] for j in range(N)]
            for i in range(N):
                for j in range(N):
                    for d in directions:
                        x, y = i + d[0], j + d[1]
                        if x < 0 or x >= N or y < 0 or y >= N:
                            continue
                        new_dp[i][j] += prev_dp[x][y]
            prev_dp = new_dp
        return sum(map(sum, prev_dp)) / float(8 ** K)

def main():

    sol = Solution()
    print(sol.knightProbability(3, 2, 0, 0))

if __name__ == "__main__":
    main()