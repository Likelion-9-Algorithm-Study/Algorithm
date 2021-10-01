import sys
sys.setrecursionlimit(10000)
f = sys.stdin.readline

m, n = map(int, f().split())
mp = [list(map(int, f().split())) for _ in range(m)]
v = [[-1] * n for _ in range(m)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1
    if v[x][y] != -1:
        return v[x][y]
    v[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and mp[nx][ny] < mp[x][y]:
            v[x][y] += dfs(nx, ny)
    return v[x][y]


print(dfs(0, 0))