import sys
f = sys.stdin.readline

v, e = map(int, f().split())
INF = int(1e9)
graph = [[INF] * (v + 1) for _ in range(v + 1)]

for i in range(e):
    a, b, c = map(int, f().split())
    graph[a][b] = c

for i in range(1, v+1):
    for j in range(1, v+1):
        for k in range(1, v+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

ans = INF

for i in range(1, v+1):
    ans = min(ans, graph[i][i])

if ans == INF: print(-1)
else: print(ans)
