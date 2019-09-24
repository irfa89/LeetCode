
def countingValleys(n, s):
    lvl , prev_lvl, valley = 0,0,0

    for step in s:
        if step == 'U':
            prev_lvl = lvl
            lvl += 1
        if step == 'D':
            prev_lvl = lvl
            lvl += -1
        if lvl == 0 and  prev_lvl < 0:
            valley += 1

    return valley

def main():
    n = int(input())
    s = list(map(str, input().split( )))
    result = countingValleys(n, s)
    print(result)

if __name__ == '__main__':
    main()