import sys, heapq
f = sys.stdin.readline

INF = int(1e9)

n, m, x = map(int, f().split())
graph = [[] for _ in range(n+1)]
d = [INF] * (n+1)

for i in range(m):
    start, dest, time = map(int, f().split())
    graph[start].append((dest, time))


def dijkstra(s):
    q = []
    d = [INF] * (n + 1)
    heapq.heappush(q, (0, s))
    d[s] = 0
    while q:
        distance, now = heapq.heappop(q)
        if d[now] < distance:
            continue
        for i in graph[now]:
            time = distance + i[1]
            if time < d[i[0]]:
                d[i[0]] = time
                heapq.heappush(q, (time, i[0]))

    return d


result = [0] * (n+1)

for i in range(1, n+1):
    res = dijkstra(i)
    if i != x:
        result[i] += res[x]
    else:
        for j in range(1, n+1):
            result[j] += res[j]

print(max(result))
