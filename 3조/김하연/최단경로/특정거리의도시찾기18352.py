import sys, heapq

f = sys.stdin.readline

INF = int(1e9)
n, m, k, x = map(int, f().split())
graph = [[] for _ in range(n + 1)]
d = [INF] * (n + 1)
for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append((b, 1))


def root():
    q = []
    heapq.heappush(q, (0, x))
    d[x] = 0
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

flag = False
for i in range(1, n + 1):
    if d[i] == k:
        print(i)
        flag = True
if not flag: print(-1)
