# 이코테 서로소집합 실전문제 2번
import sys
f = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def parent_union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, f().split())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    a, b, c = map(int, f().split())
    if a == 1:
        if find_parent(parent, b) == find_parent(parent, c):
            print("YES")
        else:
            print("NO")
    elif a == 0:
        parent_union(parent, b, c)
