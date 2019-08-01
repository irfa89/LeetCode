"""
443. Given an array of characters, compress it in-place.
The length after compression must always be smaller than or equal to the original array.
Every element of the array should be a character (not int) of length 1.
After you are done modifying the input array in-place, return the new length of the array.
"""

class Solution:

    def compress(self,l):
        s = ''.join(l)
        t = ''
        count = 1
        t += s[0]
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                if(count>1):
                    t = t + str(count)
                t = t + s[i+1]
                count = 1

        if count > 1 :
            t = t + str(count)

        return len(t),list(t)


def main():
    l = list(map(str,input("Enter caharacters :").split()))
    print(l)
    sc = Solution()
    print(sc.compress(l))


if __name__ == "__main__":
    main()