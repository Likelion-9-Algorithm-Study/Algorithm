import sys
f = sys.stdin.readline

n = int(f())
line = [list(map(int, f().split())) for _ in range(n)]
line.sort(key=lambda x: x[0])
length, last = line[0][1] - line[0][0], line[0][1]
for i in range(1, n):
    if line[i][0] >= last:
        length += line[i][1] - line[i][0]
    elif last < line[i][1]:
        length += line[i][1] - last
    last = max(last, line[i][1])

print(length)

