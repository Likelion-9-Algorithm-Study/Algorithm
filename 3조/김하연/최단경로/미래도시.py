import sys
f = sys.stdin.readline

N, M = map(int, f().split())
INF = int(1e9)
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    a, b = map(int, f().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, f().split())

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result = graph[1][K] + graph[K][X]

if result >= INF: print(-1)
else: print(result)
