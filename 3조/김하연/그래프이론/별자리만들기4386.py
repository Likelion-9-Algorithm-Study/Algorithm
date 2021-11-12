import sys, math
f = sys.stdin.readline

n = int(f())
stars, edges, ans = [], [], 0
parent = [i for i in range(n+1)]

for _ in range(n):
    x, y = map(float, f().split())
    stars.append((x, y))

for i in range(n - 1):
    for j in range(i + 1, n):
        c = math.sqrt((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) **2)
        edges.append((c, i, j))

edges.sort()

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for edge in edges:
    cost, x, y = edge
    if find_parent(x) != find_parent(y):
        ans += cost
        union(x, y)

print('%.2f' % ans)

