"""
387. Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
"""

class Solution:

    def firstUniqChar(self, s):
        t = ''
        dict = {}
        ch = list(s)

        for _ in ch:
            if _ in dict:
                dict[_] += 1
            else:
                dict[_] = 1

        for _ in ch:
            if dict.get(_) == 1:
                t = _
                break

        if t == '':
            return -1
        else:
            return ch.index(t)


def main():
    in_str = input("Enter String : ")
    sol = Solution()
    print(sol.firstUniqChar(in_str))

if __name__ == "__main__":
    main()


