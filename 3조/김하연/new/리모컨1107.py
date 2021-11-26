import sys
f = sys.stdin.readline

n = int(f())
ans = abs(100 - n)
m = int(f())
w = []
if m: w = list(f().split())

for num in range(1000001):
    for k in str(num):
        if k in w:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - n))

print(ans)
