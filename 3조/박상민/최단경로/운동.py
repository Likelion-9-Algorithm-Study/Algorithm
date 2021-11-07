# https://www.acmicpc.net/problem/1956
import sys
f = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, f().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = INF
for i in range(n):
    result = min(result, graph[i][i])
if result == INF:
    print(-1)
else:
    print(result)
