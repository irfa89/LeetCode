"""
1010. In a list of songs, the i-th song has a duration of time[i] seconds.
Return the number of pairs of songs for which their total duration in seconds is divisible by 60.
Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.
"""

class Solution:
    def numPairsDivisibleBy60(self, time):
        count, arr = 0, [0]*60

        for _ in time:
            rem = _%60
            compl = (60-rem)%60
            print(arr[compl])
            count += arr[compl]
            print(arr[rem])
            arr[rem] += 1
            print(arr[rem])

        return count

def main():
    sol = Solution()
    inp = list(map(int, input("Enter time :").split()))
    print(inp)
    print(sol.numPairsDivisibleBy60(inp))


if __name__ == "__main__":
    main()