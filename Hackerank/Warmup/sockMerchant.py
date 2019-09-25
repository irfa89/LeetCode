import math
import os
import random
import re
import sys
import unittest


def sockMerchant(n, ar):

    count, pair = 0, {}

    for i in ar:
        if i in pair:
            pair[i] += 1
        else:
            pair[i] = 1

    for k in pair:
        count += pair[k]//2

    return count



def main():
    n = int(input())
    ar = list(map(int, input().split( )))
    result = sockMerchant(n, ar)
    print(result)

if __name__ == '__main__':
    main()