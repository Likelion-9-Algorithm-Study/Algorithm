import sys
r = sys.stdin.readline

n = int(r())
res = []
for i in range(n):
    res.append(list(map(int, r().split())))

for i in range(n-2, -1, -1):
    for j in range(len(res[i])):
        res[i][j] += max(res[i+1][j], res[i+1][j+1])

print(res[0][0])
