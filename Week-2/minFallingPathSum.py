"""
931. Given a square array of integers A, we want the minimum sum of a falling path through A.
A falling path starts at any element in the first row, and chooses one element from each row.
The next row's choice must be in a column that is different from the previous row's column by
at most one
"""

class Solution:
    def minFallingPathSum(self, A):

        a,b = len(A),len(A[0])
        dp = [[0]*(b+2) for _ in range(b)]

        for i in range(a):
            dp[i][0] = dp[i][-1] = float("inf")
            for j in range(1,b+1):
                dp[i][j] = A[i][j-1]

        for i in range(1,a):
            for j in range(1,b+1):
                dp[i][j] = A[i][j-1] + min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])
        return min(dp[-1])

def main():
    sol = Solution()
    print(sol.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))

if __name__ == "__main__":
    main()