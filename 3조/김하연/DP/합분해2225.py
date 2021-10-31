import sys
f = sys.stdin.readline

n, k = map(int, f().split())
num = [[0] * (k + 1) for _ in range(n + 1)]
num[0][0] = 1
for i in range(n+1):
    for j in range(1, k+1):
        num[i][j] = (num[i-1][j] + num[i][j-1])

print(num[n][k] % 1000000000)