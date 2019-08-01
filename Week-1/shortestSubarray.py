"""
862. Return the length of the shortest, non-empty,
contiguous subarray of A with sum at least K.If there is no
non-empty subarray with sum at least K, return -1.

Leetcode : passed 60/93 test cases.

Better Way : presum

nums [1,2,3,4,5,8,-2]
presum [0,1,3,7,12,20,18]

dictionary (value = count of the value)

"""

class Solution:
    def shortestSubarray(self, A, K) :
        start, end, sum, r = 0,0,0,len(A)+1

        if len(A) == 0:
            return -1

        while start < len(A):
            while start < len(A) and sum < K:
                sum += A[start]
                start += 1
            while end < start and sum >= K:
                r = min(r,start - end)
                sum -= A[end]
                end = end +1

        return r if r != len(A) + 1 else -1


def main():

    sol = Solution()
    print(sol.shortestSubarray([2,3,1,2,4,3], 5))
    #print(sol.shortestSubarray([84,-37,32,40,95],167)) # 3

if __name__ == "__main__":

    main()

