import sys

while True:
    n = int(sys.stdin.readline())
    if n:
        dp = [[0] * (n+1) for i in range(n+1)]
        for i in range(n+1):
            dp[0][i] = 1
        for i in range(1, n+1):
            for j in range(i, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp[n][n])
    else:
        break

'''
dp[i][j] = 알약 반개 i번 알약 한개 j번
6
1
4
2
3
30
0
'''