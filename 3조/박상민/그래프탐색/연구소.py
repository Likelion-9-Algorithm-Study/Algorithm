# https://www.acmicpc.net/problem/14502
import sys
from itertools import permutations
from collections import deque
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    temp = 0
    while q_copy:
        for _ in range(len(q_copy)):
            pop_x, pop_y = q_copy.popleft()
            for i in range(4):
                nx = pop_x + dx[i]
                ny = pop_y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and a_copy[nx][ny] == 0:
                    a_copy[nx][ny] = 2
                    q_copy.append([nx, ny])

    for i in a_copy:
        if i.count(0) != 0:
            temp += i.count(0)
    return temp

candidate = []
result_list = []
temp = []
q = deque()

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            candidate.append((i, j))
        elif a[i][j] == 2:
            q.append([i, j])

max_result = 0
for e in permutations(candidate, 3):
    q_copy = copy.deepcopy(q)
    a_copy = copy.deepcopy(a)
    for w in e:
        a_copy[w[0]][w[1]] = 1
    result = bfs(m, n)
    if result > max_result:
        max_result = result

print(max_result)
