# Given an integer x, return true if x is a palindrome and false otherwise.
def is_palindrome(x):
    if x < 0 or (x > 0 and x % 10 == 0):
        # if x is negative, return False.
        # if x is positive and the last digit is 0, that also cannot form a palindrome, return False.
        return False

    result = 0
    while x > result:
        result = result * 10 + x % 10
        x = x // 10
    if x == result or x == result // 10:
        return True
    return False


if __name__ == '__main__':
    # input 1
    x = 121
    print(is_palindrome(x))
    # input 2
    x = -121
    print(is_palindrome(x))
    # input 3
    x = 10
    print(is_palindrome(x))
