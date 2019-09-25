import os

def calc_sum(a,i,j):
    return (a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j + 1] + a[i + 2][j] + a[i + 2][j + 1] + a[i + 2][j + 2])

def hourglassSum(arr):
    row, col, reference, sum = 0,0,-64,0

    for row in range(0,4):
        for col in range(0,4):
            sum = calc_sum(arr,row,col)
            reference = max(reference,sum)

    return reference



def main():
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        arr = []

        for _ in range(6):
            arr.append(list(map(int, input().rstrip().split())))

        result = hourglassSum(arr)

if __name__ == '__main__':
    main()