"""
977. Given an array of integers A sorted in non-decreasing order, return an array
of the squares of each number, also in sorted non-decreasing order.
"""


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        left, right = 0, len(A) - 1
        res = []

        while left <= right:
            if abs(A[left]) > abs(A[right]):
                res.append(A[left] * A[left])
                left += 1
            else:
                res.append(A[right] * A[right])
                right -= 1
        return res[::-1]

def main():
    sol = Solution
    #print(sol.sortedSquares([-4,-1,0,3,10]))


if __name__ == "__main__":
    main()
