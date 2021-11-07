# https://www.acmicpc.net/problem/1261
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
map_example = [list(map(str, input())) for _ in range(m)]
count = [[-1 for _ in range(n)] for _ in range(m)]
count[0][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append([0, 0])
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if count[nx][ny] == -1:
                if map_example[nx][ny] == '1':
                    q.append([nx, ny])
                    count[nx][ny] = count[x][y]+1
                elif map_example[nx][ny] == '0':
                    q.appendleft([nx, ny])
                    count[nx][ny] = count[x][y]
print(count[m-1][n-1])