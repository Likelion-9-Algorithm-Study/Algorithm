import sys
f = sys.stdin.readline

a, b = map(int, f().split())
cnt = 0

while a < b:
    if b % 2 == 0:
        b //= 2
        cnt += 1
    elif str(b)[-1] == '1':
        b = int(str(b)[:-1])
        cnt += 1
    else:
        break

if a == b: print(cnt + 1)
else: print(-1)