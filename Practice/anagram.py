import unittest

def is_anagram (str1,str2):
    first_str = list(str1)
    first_str.sort()
    second_str = list(str2)
    second_str.sort()

    if  first_str == second_str :
        return True
    else:
        return False

def main():
    first_string = map(str,input())
    second_string = map(str,input())
    res = is_anagram(first_string,second_string)
    print(res)

if __name__ == "__main__":
    main()