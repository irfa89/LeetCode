
def jumpingOnClouds(c):
    i, jumps = 0,0
    while i < len(c) -1:
        if c[i]+2 < len(c) and c[i] == 0:
            jumps += 1
            i+= 2
        else:
            jumps += 1
            i += 1
    return jumps


def main():
    c = list(map(int, input().split(",")))
    result = jumpingOnClouds(c)
    print(result)

if __name__ == '__main__':
    main()