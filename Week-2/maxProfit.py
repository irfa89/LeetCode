"""
121. Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
"""

class Solution:
    def maxProfit(self, prices) :
        if len(prices) <= 1: return 0
        minP = prices[0]
        profit = 0

        for i in range(len(prices)):
            profit = max(profit,prices[i]-minP)
            minP = min(prices[i],minP)

        return profit

def main():
    sol = Solution()
    inp = list(map(int,input("Enter Prices :").split()))
    print(inp)
    print(sol.maxProfit(inp))

if __name__ == "__main__":
    main()