import sys
f = sys.stdin.readline

n, m = map(int, f().split())
g = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, f().split())
    g[a][b] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if g[j][i] == 1 and g[i][k] == 1:
                g[j][k] = 1
ans = 0
for i in range(1, n+1):
    t = 0
    for j in range(1, n+1):
        t += g[i][j] + g[j][i]
    if t == n - 1:
        ans += 1
print(ans)