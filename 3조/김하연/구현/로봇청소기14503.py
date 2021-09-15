import sys
f = sys.stdin.readline

n, m = map(int, f().split())
r, c, d = map(int, f().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
room = [list(map(int, f().split())) for _ in range(n)]
room[r][c] = 2
cnt = 1

while True:
    flag = False
    for i in range(4):
        d = (d-1) % 4
        nx, ny = r + dx[d], c + dy[d]
        if 0 < nx < n and 0 < ny < m:
            if room[nx][ny] == 0:
                room[nx][ny] = 2
                r, c = nx, ny
                cnt += 1
                flag = True
                break
    if not flag:
        nx, ny = r - dx[d], c - dy[d]
        if 0 < nx < n and 0 < ny < m:
            if room[nx][ny] == 2:
                r, c = nx, ny
            elif room[nx][ny] == 1:
                break
        else:
            break

print(cnt)






