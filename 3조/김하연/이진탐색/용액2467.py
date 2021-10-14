import sys
f = sys.stdin.readline

n = int(f())
num = sorted(list(map(int, f().split())))
left, right, ans = 0, n-1, [sys.maxsize * 10, []]

while left < right:
    cur = num[left] + num[right]
    if abs(cur) < ans[0]:
        ans = [abs(cur), [num[left], num[right]]]
    if cur < 0:
        left += 1
    elif cur > 0:
        right -= 1
    else:
        break

print(*ans[1])
