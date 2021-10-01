import sys
f = sys.stdin.readline

r, c = map(int, f().split())
board = [str(f().strip()) for _ in range(r)]
stack = set([(0, 0, '')])
result = 0
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

while stack:
    rc, cc, passed = stack.pop()
    if board[rc][cc] not in passed:
        passed_c = passed + board[rc][cc]
        result = max(result, len(passed_c))
        for i in range(4):
            nr = rc + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < r and 0 <= nc < c and board[nr][nc] not in passed_c:
                stack.add((nr, nc, passed_c))

print(result)