import sys
from collections import deque
f = sys.stdin.readline

n = int(f())
indegree = [0] * (n+1)
g, dp = [[] for _ in range(n+1)], [0] * (n+1)
c, q = [0] * (n+1), deque([])
for i in range(1, n+1):
    t = list(map(int, f().split()))
    c[i] = t[0]
    for x in t[1:-1]:
        indegree[i] += 1
        g[x].append(i)

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = c[i]

while q:
    cur = q.popleft()
    for i in g[cur]:
        indegree[i] -= 1
        dp[i] = max(dp[i], c[i] + dp[cur])
        if indegree[i] == 0:
            q.append(i)

for i in range(1, n+1):
    print(dp[i])


