# https://www.acmicpc.net/problem/2458
import sys
f = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, f().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] == 1 or (graph[a][k] == 1 and graph[k][b] == 1):
                graph[a][b] = 1

answer = 0
for i in range(1, n+1):
    temp = 0
    for j in range(1, n+1):
        temp += graph[i][j] + graph[j][i]
    if temp == n-1:
        answer += 1
print(answer)