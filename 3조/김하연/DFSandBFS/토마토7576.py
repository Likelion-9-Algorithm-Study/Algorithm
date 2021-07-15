import sys
from collections import deque


def bfs(m,n,tomato):
    cnt = -1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while q:
        cnt+=1
        for _ in range(len(q)):
            tx, ty = q.popleft()
            for i in range(4):
                x = tx+dx[i]
                y = ty+dy[i]
                if 0 <= x < N and 0 <= y < M and tomato[x][y]==0:
                    tomato[x][y] = tomato[tx][ty]+1
                    q.append((x,y))
    for t in tomato:
        if 0 in t:
            return -1
        
    return cnt

M, N = map(int,sys.stdin.readline().split())
tomato, q = [], deque([])
for i in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    for j in range(M):
        if row[j] == 1:
            q.append((i,j))
    tomato.append(row)

print(bfs(M,N,tomato))