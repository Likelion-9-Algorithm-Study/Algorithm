import sys
f = sys.stdin.readline


def quasi(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def palindrome(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if quasi(s, left+1, right) or quasi(s, left, right-1):
                return 1
            else:
                return 2
    return 0


t = int(f())
for _ in range(t):
    string = f().strip()
    print(palindrome(string, 0, len(string)-1))