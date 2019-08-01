"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
"""

class Solution:
    def trap(self, height):
        left_max,sum,right_max = 0,0,0

        left_HH = [0 for i in range(len(height))]

        for i in range(len(height)):
            if height[i] > left_max : left_max = height[i]
            left_HH[i] = left_max

        for i in reversed(range(len(height))):
            if height[i] > right_max : right_max = height[i]
            if min(right_max,left_HH[i]) > height[i]:
                sum += min(right_max,left_HH[i]) - height[i]

        return sum




def main():
    sol = Solution()
    print("Water Stored :",sol.trap(list(map(int,input("Enter heights :").split()))))

if __name__ == "__main__":
    main()
