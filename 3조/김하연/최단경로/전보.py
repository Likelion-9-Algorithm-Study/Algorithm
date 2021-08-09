import sys, heapq

f = sys.stdin.readline

INF = int(1e9)

N, M, C = map(int, input().split())

graph = [[] for i in range(N + 1)]
d = [INF] * (N + 1)

for i in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))


def root():
    q = []
    heapq.heappush(q, (0, C))
    d[C] = 0

    while q:
        distance, now = heapq.heappop(q)
        if d[now] < distance:
            continue
        for i in graph[now]:
            cost = distance + i[1]
            if d[i[0]] > cost:
                d[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


root()

count, max_d = 0, 0

for i in d:
    if i < INF:
        count += 1
        max_d = max(max_d, i)

print(count - 1, max_d)
