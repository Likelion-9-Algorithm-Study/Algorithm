import sys, copy
N = int(input())
rgb = []
for i in range(N):
    rgb.append(list(map(str,sys.stdin.readline().strip())))
rgb2 = copy.deepcopy(rgb)
for i in range(N):
    for j in range(N):
        if rgb2[i][j] == 'G': rgb2[i][j] = 'R'

def dfs(x,y,c,color):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    prev = c
    stack = [(x,y)]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i] 
            if 0 <= nx < N and 0 <= ny < N and color[nx][ny] == prev :
                color[nx][ny] = -1
                stack.append((nx,ny))

normal, blind = 0, 0
for i in range(N):
    for j in range(N):
        if rgb[i][j]!=-1:
            dfs(i,j,rgb[i][j],rgb)
            normal+=1
        if rgb2[i][j]!=-1:
            dfs(i,j,rgb2[i][j],rgb2)
            blind+=1
print(normal,blind)

        


    