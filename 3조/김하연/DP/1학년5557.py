import sys
f = sys.stdin.readline

n = int(f())
num = list(map(int, f().split()))
dp = [[0] * 21 for _ in range(n)]
dp[0][num[0]] = 1

for i in range(1, n-1):
    for j in range(21):
        if dp[i-1][j]:
            if 0 <= j + num[i] <= 20: dp[i][j+num[i]] += dp[i-1][j]
            if 0 <= j - num[i] <= 20: dp[i][j-num[i]] += dp[i-1][j]

print(dp[n-2][num[-1]])

# dp[i][j] num에서 i번째 인덱스까지 계산했을 때 j가 나올 수 있는 경우의 수