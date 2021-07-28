import sys
from collections import deque

r = sys.stdin.readline

N, M = map(int, r().split())
bridge = [[] for _ in range(N + 1)]
for i in range(M):
    a, b, c = map(int, r().split())
    bridge[a].append((b, c))
    bridge[b].append((a, c))

start, dest = map(int, r().split())
minimum, maximum = 1, 1000000000


def bfs(mid):
    q = deque([start])
    visited = [start]
    while q:
        s = q.popleft()
        if s == dest:
            return True
        for tb, tc in bridge[s]:
            if tb not in visited and mid <= tc:
                q.append(tb)
                visited.append(tb)
    return False


while minimum <= maximum:
    mid = (minimum + maximum) // 2
    if bfs(mid):
        minimum = mid + 1
    else:
        maximum = mid - 1
print(maximum)

'''
3 3
1 2 4
1 3 3
2 3 5
1 3
'''
