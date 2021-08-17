import sys
from collections import deque
import copy

f = sys.stdin.readline

n = int(f())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)

for i in range(1, n+1):
    inp = list(map(int, f().split()))
    time[i] = inp[0]
    for j in range(1, len(inp)-1):
        indegree[i] += 1
        graph[inp[j]].append(i)

q = deque([])
result = copy.deepcopy(time)
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    for i in graph[cur]:
        result[i] = max(result[i], result[cur]+time[i])
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

for i in range(1, n+1):
    print(result[i])


'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''