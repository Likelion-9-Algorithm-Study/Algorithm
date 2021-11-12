# # https://www.acmicpc.net/problem/4386
import heapq
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

n = int(input())
parent = [i for i in range(n+1)]
stars = list(tuple(map(float, input().split())) for _ in range(n))

result = []
for i in range(n-1):
    for j in range(i+1, n):
        heapq.heappush(result, (((stars[i][0]-stars[j][0])**2 + (stars[i][1]-stars[j][1])**2) ** 0.5, i, j))

answer = 0
while result:
    cost, a, b = heapq.heappop(result)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += cost

print(round(answer, 2))