import sys
from collections import deque

f = sys.stdin.readline

n, m = map(int, f().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, f().split())
    indegree[b] += 1
    graph[a].append(b)

q = deque([])
res = []

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    res.append(now)
    for x in graph[now]:
        indegree[x] -= 1
        if indegree[x] == 0:
            q.append(x)


for i in res:
    print(i, end=' ')
