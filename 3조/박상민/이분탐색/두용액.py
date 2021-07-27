# https://www.acmicpc.net/problem/2470
import sys
f = sys.stdin.readline

n = int(f())
a = [x for x in map(int, f().split())]
a.sort()

start = 0
end = len(a) - 1
target = 0
ans = [(a[start], a[end], a[start]+a[end])]
for i in range(len(a)):
    if start != end:
        cur = a[start] + a[end]
        if abs(ans[0][2]) >= abs(cur):
            ans.pop()
            ans.append([a[start], a[end], cur])
        if cur > target:
            end -= 1
        elif cur < target:
            start += 1
        else:
            break

print(ans[0][0], ans[0][1])
