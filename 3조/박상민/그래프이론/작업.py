# https://www.acmicpc.net/problem/2056
import sys
from collections import deque
input = sys.stdin.readline

q = deque()
n = int(input())
indegree = [0] * (n+1)
times = [0] * (n+1)
dp = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    tower = list(map(int, input().split()))
    times[i] = tower[0]
    indegree[i] += tower[1]
    for j in tower[2:]:
        graph[j].append(i)

for i in range(1, n+1):
    if indegree[i] == 0:
        dp[i] = times[i]
        q.append(i)

while q:
    now = q.popleft()
    for i in graph[now]:
        indegree[i] -= 1
        dp[i] = max(dp[i], dp[now] + times[i])
        if indegree[i] == 0:
            q.append(i)

print(max(dp))