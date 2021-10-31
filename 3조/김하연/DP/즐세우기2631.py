import sys

f = sys.stdin.readline

n = int(f())
kids = [int(f()) for _ in range(n)]
dp = [0] * n

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if kids[i] > kids[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))

# 가장 긴 증가하는 부분수열을 찾아내고 나머지 남은 수들을 하나씩 제자리에 배치하면 된다
