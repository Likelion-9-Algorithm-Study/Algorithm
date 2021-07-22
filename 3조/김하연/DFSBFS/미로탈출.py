import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
maze = []
for i in range(N):
    maze.append(list(map(int,str(input().strip()))))

def bfs(n,m):
    q = deque([(n,m,1)])
    maze[n][m] = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        n, m, count = q.popleft()
        count += 1
        for i in range(4):
            nx = m + dx[i]
            ny = n + dy[i]
            if ny == N-1 and nx == M-1:
                return count
            if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] == 1:
                maze[ny][nx] = 0
                q.append((ny,nx,count))
    return count

print(bfs(0,0))