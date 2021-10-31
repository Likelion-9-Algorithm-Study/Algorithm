# https://www.acmicpc.net/problem/4811
import sys
input = sys.stdin.readline

while True:
    a = int(input())
    if a != 0:
        dp = [[0 for _ in range(a + 1)] for _ in range(a + 1)]
        for i in range(a + 1):
            for j in range(i, a + 1):
                if i == 0:
                    dp[i][j] = 1
                elif i == 1:
                    dp[i][j] = j
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(dp[-1][-1])
    else:
        break
