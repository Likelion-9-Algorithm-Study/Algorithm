import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
ice = []
for i in range(N):
    ice.append(list(map(int,str(input().strip()))))

def bfs(n,m):
    q = deque([(n,m)])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    ice[n][m] = 1
    while q:
        n, m = q.popleft()
        for i in range(4):
            nx = m + dx[i]
            ny = n + dy[i]
            if 0 <= nx < M and 0 <= ny < N and ice[ny][nx] == 0:
                ice[ny][nx] = 1
                q.append((ny,nx))
count = 0
for i in range(N):
    for j in range(M):
        if ice[i][j] == 0:
            bfs(i,j)
            count += 1
print(count)

'''
00110
00011
11111
00000
'''