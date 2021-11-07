# https://www.acmicpc.net/problem/13549
import sys
from collections import deque

visited = [0 for _ in range(100001)]
n, k = map(int, sys.stdin.readline().split())

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return visited[v]
        else:
            for i in (v-1, v+1, 2*v):
                if 0 <= i <= 100000 and not visited[i] and i != n:
                    if i != 2*v:
                        q.append(i)
                        visited[i] = visited[v] + 1
                    else:
                        q.appendleft(i)
                        visited[i] = visited[v]
print(bfs(n))
