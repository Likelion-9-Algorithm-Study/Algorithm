import sys
f = sys.stdin.readline

n, k = map(int, f().split())
num = list(map(int, f().strip()))
cnt, res = 0, []

for i in range(n):
    while cnt < k and res:
        if res[-1] < num[i]:
            res.pop()
            cnt += 1
        else:
            break
    res.append(num[i])

for i in range(n-k):
    print(res[i], end='')