import sys
input = sys.stdin.readline

N = int(input())
p, n, sum = [], [], 0

for i in range(N):
    num = int(input())

    if num > 1: p.append(num)
    elif num == 1: sum+=1
    else: n.append(num)

p.sort(reverse=True)
n.sort()

if len(p)%2 == 0:
    for i in range(0,len(p),2):
        sum += p[i]*p[i+1]
else:
    for i in range(0,len(p)-1,2):
        sum += p[i]*p[i+1]
    sum += p[-1]
if len(n)%2 == 0:
    for i in range(0,len(n),2):
        sum += n[i]*n[i+1]
else:
    for i in range(0,len(n)-1,2):
        sum += n[i]*n[i+1]
    sum += n[-1]
print(sum)


