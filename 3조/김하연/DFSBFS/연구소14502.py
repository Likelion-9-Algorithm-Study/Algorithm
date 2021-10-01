import sys, copy
f = sys.stdin.readline

n, m = map(int, f().split())
room = [list(map(int, f().split())) for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
max_safe = 0
virus = [(i, j) for j in range(m) for i in range(n)]


def spread(r, c, room_c):
    if room_c[r][c] == 2:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if room_c[nr][nc] == 0:
                    room_c[nr][nc] = 2
                    spread(nr, nc, room_c)


def wall(start, cnt):
    global max_safe
    if cnt == 3:
        room_c = copy.deepcopy(room)
        for v in virus:
            r, c = v
            spread(r, c, room_c)
        safe_cnt = sum(x.count(0) for x in room_c)
        max_safe = max(max_safe, safe_cnt)

    else:
        for i in range(start, n*m):
            row = i // m
            col = i % m
            if room[row][col] == 0:
                room[row][col] = 1
                wall(i, cnt+1)
                room[row][col] = 0


wall(0, 0)
print(max_safe)
