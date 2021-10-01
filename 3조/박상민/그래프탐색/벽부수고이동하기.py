# https://www.acmicpc.net/problem/2206
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque([[0, 0, 1]])
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    while q:
        x, y, w = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if location[nx][ny] and w:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    q.append([nx, ny, 0])
                elif not location[nx][ny] and not visited[nx][ny][w]:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append([nx, ny, w])
    return -1
n, m = list(map(int, input().split()))
location = [list(map(int, input().rstrip())) for _ in range(n)]
print(bfs())