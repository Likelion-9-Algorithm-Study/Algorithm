import sys, heapq
f = sys.stdin.readline

INF = int(1e9)
V, E = map(int, f().split())
start = int(f())
graph = [[] for _ in range(V+1)]
d = [INF] * (V+1)

for i in range(E):
    u, v, w = map(int, f().split())
    graph[u].append((v, w))


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

for i in range(1, V+1):
    if d[i] != INF:
        print(d[i])
    else:
        print('INF')


'''
5 6
3
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
'''