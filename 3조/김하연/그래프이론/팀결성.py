import sys
f = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:   parent[b] = a
    else: parent[a] = b


n, m = map(int, f().split())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    t, a, b = map(int, f().split())
    if t == 0:
        union_parent(parent, a, b)
    else:
        pa = find_parent(parent, a)
        pb = find_parent(parent, b)
        if pa == pb: print('YES')
        else: print('NO')



'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''


