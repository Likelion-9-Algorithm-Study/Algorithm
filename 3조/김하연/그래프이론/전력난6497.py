import sys
f = sys.stdin.readline

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

while True:
    m, n = map(int, f().split())
    if m == 0 and n == 0:
        break
    edges, houses, ans, total = [], [], 0, 0
    parent = [i for i in range(m)]
    for _ in range(n):
        x, y, z = map(int, f().split())
        edges.append((z, x, y))
        total += z
    edges.sort()
    for edge in edges:
        z, x, y = edge
        if find_parent(x) != find_parent(y):
            ans += z
            union(x, y)
    print(total-ans)
