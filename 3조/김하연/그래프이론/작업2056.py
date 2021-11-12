import sys, heapq
from collections import deque
input = sys.stdin.readline

n = int(input())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
c = [0] * (n+1)

for i in range(1,n+1):
    t = list(map(int, input().split()))
    cost, cnt, pre_list = t[0], t[1], t[2:]
    c[i] = cost
    for x in pre_list:
        graph[x].append(i)
        indegree[i] += 1

def topology_sort():
    q = deque([])
    dp = [0] * (n+1)
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = c[i]
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            indegree[i] -= 1
            dp[i] = max(dp[i], c[i]+dp[cur])
            if indegree[i] == 0:
                q.append(i)
    return max(dp)

print(topology_sort())







