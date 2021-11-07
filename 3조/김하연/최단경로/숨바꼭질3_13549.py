import sys
from collections import deque
f = sys.stdin.readline

n, k = map(int, f().split())
q = deque([(n, 0)])
visit = [0] * 100001

while q:
    x, c = q.popleft()
    if not visit[x]: visit[x] = 1
    if x == k:
        print(c)
        break
    if 0 <= x-1 <= 100000 and not visit[x-1]: q.append((x-1, c+1))
    if 0 <= x+1 <= 100000 and not visit[x+1]: q.append((x+1, c+1))
    if 0 <= x*2 <= 100000 and not visit[x*2]: q.appendleft((x*2, c)) # 0초 후이므로 가장 우선순위 높음


