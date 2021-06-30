import sys
n = int(input())
meet = []
for i in range(n):
    meet.append(list(map(int,sys.stdin.readline().split())))
meet.sort(key=lambda x: x[0])
meet.sort(key=lambda x: x[1])
count, last = 1, meet[0]
for i in range(1,n):
    if meet[i][0]>=last[1]:
        count+=1
        last = meet[i]
print(count)
