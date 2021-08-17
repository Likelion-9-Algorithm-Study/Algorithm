import sys, copy
from collections import deque
f = sys.stdin.readline

T = int(f())

for _ in range(T):
    n, k = map(int, f().split())
    time = list(map(int, f().split()))
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]

    for _ in range(k):
        x, y = map(int, f().split())
        indegree[y] += 1
        graph[x].append(y)

    target = int(f())
    q = deque([])

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    result = copy.deepcopy(time)

    while q:
        now = q.popleft()
        for x in graph[now]:
            indegree[x] -= 1
            result[x-1] = max(result[x-1], time[x-1] + result[now-1])
            if indegree[x] == 0:
                q.append(x)

    print(result[target-1])


