# https://www.acmicpc.net/problem/2631
import sys
input = sys.stdin.readline

a = int(input())
b = [int(input()) for _ in range(a)]

dp = [1] * 201

for i in range(a):
    for j in range(i):
        if b[i] > b[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(a-max(dp))