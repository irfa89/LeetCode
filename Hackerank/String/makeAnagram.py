import math
import os
import random
import re
import sys


def makeAnagram(a, b):
    cnt = [0] * 26
    offset = ord('a')
    for char in a:
        cnt[ord(char) - offset] += 1
    for char in b:
        cnt[ord(char) - offset] -= 1
    total = 0
    for value in cnt:
        total += abs(value)
    return total


def main():
    a = input()
    b = input()
    res = makeAnagram(a, b)
    print(res)

if __name__ == '__main__':
    main()
