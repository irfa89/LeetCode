"""
209. Given an array of n positive integers and a positive integer s, find the minimal length of a
contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

"""

class Solution:
    def minSubArrayLen(self, s, nums):
        i, j, sum, r = 0, 0, 0, len(nums) + 1
        if len(nums) == 0:
            return 0

        while j < len(nums):
            while j < len(nums) and sum < s:
                sum += nums[j]
                j += 1
            while i < j and sum >= s:
                r = min(r, j - i)
                sum -= nums[i]
                i += 1

        return r if r != len(nums) + 1 else 0



def main():
    sol = Solution()
    s = 7
    nums = [2,3,1,2,4,3]
    #print(sol.minSubArrayLen(map(int,input("Enter sum : ")),list(map(int,input("Enter list :").split()))))
    print(sol.minSubArrayLen(s,nums))

if __name__ == "__main__":
    main()
