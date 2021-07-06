import sys
from collections import defaultdict
n = int(sys.stdin.readline())
board = defaultdict(list)

while True:
    a, b = list(map(int, sys.stdin.readline().split()))
    if a == -1 and b == -1:
        break
    board[a].append(b)
    board[b].append(a)

score = [0] * (n+1)


def bfs():
    for i in range(1, n+1):
        visited = [False] * (n+1)
        count = -1
        need_visit = [i]

        while need_visit:
            temp_list = []
            for j in need_visit:
                visited[j] = True
                for k in board[j]:
                    if visited[k] == False:
                        temp_list.append(k)
                        visited[k] = True
            count += 1
            need_visit = list(temp_list)
        score[i] = count
    min_score = min(score[1:])
    order = []
    for i in range(1, len(score)):
        if score[i] == min_score:
            order.append(i)
    print(min_score, len(order))
    order.sort()
    print(*order)
    return


bfs()
