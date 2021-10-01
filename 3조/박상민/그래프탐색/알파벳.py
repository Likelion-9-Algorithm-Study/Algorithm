# https://www.acmicpc.net/problem/1987
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

alphabet = [list(map(str, list(str(input().rstrip())))) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global result
    q = {(x, y, alphabet[x][y])}
    while q:
        pop_x, pop_y, ans = q.pop()
        for i in range(4):
            nx = pop_x + dx[i]
            ny = pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and alphabet[nx][ny] not in ans:
                q.add((nx, ny, ans+alphabet[nx][ny]))
                result = max(result, len(ans)+1)

result = 1
bfs(0, 0)
print(result)
