# 백준 12865번 평범한 배낭
from sys import stdin
input = stdin.readline
n, k = map(int, input().split())
arr = []
dp = [0] * (k+1)        # index : 무게
for _ in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))
    
arr.sort()
weights = []
values = []
for i in range(len(arr)):
    w, v = arr[i]
    weights.append(w)
    values.append(v)
    

def knapsack_bottomUp(weights, values, k, n):
    dp = [0 for i in range(k+1)]
    
    for i in range(n):
        now = weights[i]
        # print("weights[i]:", now)
        for w in range(k, 0, -1):
            if now <= w:
                dp[w] = max(dp[w], dp[w-now]+values[i])
                # print(dp)
    return dp[k]

print(knapsack_bottomUp(weights, values, k, n))
# dp = [[-1]*(k+1) for _ in range(n+1)]
# def knapsack_memo(weights, values, k, n):
#     global dp
    
#     if n == 0 or k == 0:
#         return 0
#     if dp[n][k] != -1:
#         return dp[n][k]
    
    
#     if weights[n-1] <= k:
#         included = values[n-1]+knapsack_memo(weights, values, k-weights[n-1], n-1)
#         excluded = knapsack_memo(weights, values, k, n-1)
#         dp[n][k] = max(included, excluded)
#         return dp[n][k]
#     else: # weights[n-1] > k
#         dp[n][k] = knapsack_memo(weights, values, k, n-1)
#         return dp[n][k]
# print(knapsack_memo(weights, values, k, n))

# def knapsack(k, weights, values, n):
#     if n == 0 or k == 0:
#         return 0
    
#     if (weights[n-1]) > k:
#         return knapsack(k, weights, values, n-1)
#     else:
#         # included = values[n-1] + knapsack(k-weights[n-1], weights, values, n-1)
#         # unincluded = knapsack(k, weights, values, n-1)
#         # result = max(included, unincluded)
#         return max(values[n-1] + knapsack(k-weights[n-1], weights, values, n-1), knapsack(k, weights, values, n-1))
    
# print(knapsack(k, weights, values, n))

# 4 5
# 1 4
# 1 8
# 3 3
# 4 8
# n\k 0   1   2   3   4   5
# 0 [-1, -1, -1, -1, -1, -1],
# 1 [-1, 4, 4, -1, 4, 4],
# 2 [-1, 8, 12, -1, -1, 12],
# 3 [-1, 8, -1, -1, -1, 15],
# 4 [-1, -1, -1, -1, -1, 16]]