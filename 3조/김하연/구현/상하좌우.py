import sys

n = int(input())
plan = list(sys.stdin.readline().split())
current = [1,1]

for i in plan:
    if i == 'L':
        if current[1] != 1:
            current[1]-=1
    if i == 'R':
        if current[1] != n:
            current[1]+=1
    if i == 'U':
        if current[0] != 1:
            current[0]-=1
    if i == 'D':
        if current[0] != n:
            current[0]+=1
for i in current: print(i, end=' ')