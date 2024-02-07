def valid_palindrome(s):
    flag = 0
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        elif flag < 1:
            if s[left] == s[right - 1]:
                flag = 1
                right -= 1
            elif s[left + 1] == s[right]:
                flag = 1
                left += 1
        else:
            return False

    return True


if __name__ == '__main__':

    # input 1
    s = "aba"
    print(valid_palindrome(s))
    s = "abca"
    print(valid_palindrome(s))
    s = "abc"
    print(valid_palindrome(s))
