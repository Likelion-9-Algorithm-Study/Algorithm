import sys
f = sys.stdin.readline

n, h = map(int, f().split())
top, bot, ans = [[0] * (h + 1) for _ in range(3)]
for i in range(n):
    inp = int(f())
    if i % 2: top[inp] += 1
    else: bot[h - inp + 1] += 1

for i in range(h-1, 0, -1):
    top[i] += top[i + 1]
for i in range(1, h+1):
    bot[i] += bot[i - 1]
for i in range(1, h+1):
    ans[i] = top[i] + bot[i]
ans = ans[1:]
cnt = min(ans)
print(cnt, ans.count(cnt))