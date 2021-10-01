import sys
from collections import deque
f = sys.stdin.readline

n, m = map(int, f().split())
mp = [list(map(int, str(f().strip()))) for _ in range(n)]

def bfs():
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    q = deque([(0, 0, 1)])
    visit = [[[0] * 2 for j in range(m)] for i in range(n)]
    visit[0][0][1] = 1

    while q:
        x, y, w = q.popleft()
        if x == n-1 and y == m-1:
            return visit[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if mp[nx][ny] == 1 and w == 1:
                    visit[nx][ny][0] = visit[x][y][w] + 1
                    q.append((nx, ny, 0))
                elif mp[nx][ny] == 0 and visit[nx][ny][w] == 0:
                    visit[nx][ny][w] = visit[x][y][w] + 1
                    q.append((nx, ny, w))
    return -1

print(bfs())

