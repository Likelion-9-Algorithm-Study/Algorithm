import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

for i in range(T):
    n = int(input())
    log = list(map(int,input().split()))
    log = deque(sorted(log))
    left, right, result = log.popleft(), log.popleft(), 0
    while log:
        temp_left = log.popleft()
        if not log:
            result = max(abs(temp_left - left), result)
            break
        temp_right = log.popleft()
        result = max(abs(temp_left - left), abs(temp_right - right), result)
        left = temp_left
        right = temp_right
    print(result)
'''
for i in range(T):
    n = int(input())
    log = list(map(int,input().split()))
    log.sort()
    result = 0
    for i in range(2,n):
        result = max(result, abs(log[i]-log[i-2]))
    print(result)


'''
