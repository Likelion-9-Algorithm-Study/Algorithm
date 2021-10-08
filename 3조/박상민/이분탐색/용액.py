# https://www.acmicpc.net/problem/2467
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

start = 0
end = len(a)-1
target = 0
ans = [(a[start], a[end], a[start]+a[end])]
for i in range(len(a)):
    if start != end:
        cur = a[start] + a[end]
        if abs(ans[0][2]) > abs(cur):
            ans.pop()
            ans.append((a[start], a[end], cur))
        if cur > 0:
            end -= 1
        elif cur < 0:
            start += 1
        else:
            break

print(ans[0][0], ans[0][1])