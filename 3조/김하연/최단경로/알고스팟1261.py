import sys
import heapq
f = sys.stdin.readline

m, n = map(int, f().split())
room = [list(map(int, str(f().strip()))) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
q = [(0, 0, 0)]

while q:
    w, r, c = heapq.heappop(q)
    if c == m-1 and r == n-1:
        print(w)
        break
    for i in range(4):
        nc = c + dx[i]
        nr = r + dy[i]
        if 0 <= nc < m and 0 <= nr < n and not visited[nr][nc]:
            visited[nr][nc] = 1
            if room[nr][nc] == 1:
                heapq.heappush(q, (w+1, nr, nc))
            else:
                heapq.heappush(q, (w, nr, nc))

