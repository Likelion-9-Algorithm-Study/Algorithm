
from collections import deque
N, K = map(int,input().split())

def bfs(v):
    count = 0
    q = deque([(v,count)])
    visited = []
    while q:
        v, count = q.popleft()
        if v not in visited:
            visited.append(v)
            if v == K:  return count
            count+=1
            if v*2 <= 100000: q.append((v*2,count))
            if v+1 <= 100000: q.append((v+1,count))
            if v-1 >= 0: q.append((v-1,count))
    return count

print(bfs(N))
