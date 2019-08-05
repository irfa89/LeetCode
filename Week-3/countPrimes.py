"""
204. Count the number of prime numbers
less than a non-negative number, n.
"""

class Solution:
    def countPrimes(self, n):

        if n <= 2:
            return 0

        isprime = [1] * n
        for i in range(2, n):
            if isprime[i] == 1:
                j = 2 * i
                while j < n:
                    isprime[j] = 0
                    j += i
        return sum(isprime) - 2


def main():
    sol = Solution()
    print(sol.countPrimes(10))


if __name__ == "__main__":
    main()
