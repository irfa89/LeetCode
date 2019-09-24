
def repeatedString(s, n):
    char_str = list(s)
    a_count = 0
    for char in char_str:
        if char == 'a':
            a_count += 1
    divisor = n // len(char_str)
    tot_count = divisor * a_count
    remainder = n%len(char_str)

    for i in range(0,remainder):
        if char_str[i] == 'a' :
            tot_count += 1

    return tot_count

def main():
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    print(result)

if __name__ == '__main__':
    main()