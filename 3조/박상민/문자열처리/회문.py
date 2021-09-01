import sys
f = sys.stdin.readline
a = int(f())



def is_palindrome(x, left, right):
    while left < right:
        if x[left] == x[right]:
            left += 1
            right -= 1
        else:
            left_check = one_check(x, left+1, right)
            right_check = one_check(x, left, right-1)

            if left_check or right_check:
                return 1
            else:
                return 2
    return 0

def one_check(x, left, right):
    while left < right:
        if x[left] == x[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

for i in range(a):
    x = f().rstrip()
    left = 0
    right = len(x) - 1
    print(is_palindrome(x, left, right))
