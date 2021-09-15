import sys
from collections import deque
f = sys.stdin.readline

n = int(f())
board = [[0] * (n+1) for _ in range(n+1)]
k = int(f())
for _ in range(k):
    a, b = map(int, f().split())
    board[a][b] = 1
l = int(f())
turn = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, -0]
for _ in range(l):
    x, c = f().split()
    turn.append((int(x), c))

time, d, idx = 0, 0, 0
x, y, = 1, 1
q = deque([(x, y)])

while True:
    nx = x + dx[d]
    ny = y + dy[d]
    time += 1
    if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] != 2:
        if board[nx][ny] == 0:
            board[nx][ny] = 2
            q.append((nx, ny))
            tx, ty = q.popleft()
            board[tx][ty] = 0
        if board[nx][ny] == 1:
            board[nx][ny] = 2
            q.append((nx, ny))
    else:
        break
    x, y = nx, ny
    if idx < l and time == turn[idx][0]:
        if turn[idx][1] == 'D':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
        idx += 1

print(time)