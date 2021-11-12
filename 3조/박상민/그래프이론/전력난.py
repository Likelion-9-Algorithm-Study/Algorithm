# https://www.acmicpc.net/problem/6497
import sys
f = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

while True:
    v, e = map(int, f().split())
    if v == 0 and e == 0:
        break
    else:
        parent = [0] * (v+1)
        edges = []
        result = 0

        for i in range(1, v+1):
            parent[i] = i

        temp = 0
        for _ in range(e):
            a, b, cost = map(int, f().split())
            edges.append((cost, a, b))
            temp += cost
        edges.sort()

        for i in edges:
            cost, a, b = i
            if find_parent(parent, a) != find_parent(parent, b):
                union_parent(parent, a, b)
                result += cost

        print(temp-result)
