import sys
sys.setrecursionlimit(20000)
def dfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        if 0 <= tx < N  and 0 <= ty < M:
            if field[tx][ty] == 1:
                field[tx][ty] = 0
                dfs(tx,ty)
T = int(input())
for _ in range(T):
    M, N, K = map(int,sys.stdin.readline().split())
    field = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int,sys.stdin.readline().split())
        field[y][x] = 1
    count = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] > 0:
                dfs(i,j)
                field[i][j] = 0
                count+=1
    print(count)
                


