# 이분 탐색 범위 줄이는 방법 질문 하기
import sys
from collections import defaultdict
n, m = list(map(int, sys.stdin.readline().split()))
board = defaultdict(int)

low = 0
high = float('inf')

for i in range(n):
    temp = int(sys.stdin.readline())
    board[temp] += 1
    if board[temp] * m < high:
        high = temp * m // board[temp]


result = high
while low <= high:
    temp = m
    mid = (low + high) // 2
    for i in board.keys():
        if i < mid:
            temp -= (mid // i) * board[i]
    if temp > 0:
        low = mid + 1
    elif temp <= 0:
        high = mid - 1
        if result > mid:
            result = mid

print(result)

# import sys
# import heapq
# n, m = list(map(int, sys.stdin.readline().split()))
# board = []
# result = 0
# for i in range(n):
#     temp = int(sys.stdin.readline())
#     heapq.heappush(board, [temp, temp])

# while m > 0:
#     temp = heapq.heappop(board)
#     heapq.heappush(board, [temp[0]+temp[1], temp[1]])
#     if temp[0] > result:
#         result = temp[0]
#     # print(temp)
#     m -= 1
# print(result)
