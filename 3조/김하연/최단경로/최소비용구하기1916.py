import sys, heapq
f = sys.stdin.readline

INF = int(1e9)
n = int(f())
m = int(f())
graph = [[] for _ in range(n+1)]
d = [INF] * (n+1)

for i in range(m):
    u, v, w = map(int, f().split())
    graph[u].append((v, w))

start, dest = map(int, f().split())


def dijkstra():
    q = []
    heapq.heappush(q, (0, start))
    d[start] = 0
    while q:
        distance, now = heapq.heappop(q)
        if d[now] < distance:
            continue
        for i in graph[now]:
            cost = distance + i[1]
            if cost < d[i[0]]:
                d[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra()

print(d[dest])


