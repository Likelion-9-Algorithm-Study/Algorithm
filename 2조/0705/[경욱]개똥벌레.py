import sys
from collections import defaultdict
input = sys.stdin.readline
n, h = list(map(int, input().split()))
up, down = [0] * (h+1), [0] * (h+1)

for i in range(n):
    temp = int(input())
    if i % 2 == 0:  # 아래
        down[temp] += 1
    else:  # 위
        up[temp] += 1
print(up)
print(down)
for i in range(len(up)-2, -1, -1):
    up[i] += up[i+1]
    down[i] += down[i+1]

print(up)
print(down)

low = 0
high = h
result_min = float('inf')
result_count = 0

for i in range(1, len(up)):
    temp_count = down[i] + up[-(i-h-1)]
    if temp_count < result_min:
        result_min = temp_count
        result_count = 1
    elif temp_count == result_min:
        result_count += 1
print(result_min, result_count)


# import sys

# from collections import defaultdict
# input = sys.stdin.readline
# n, h = list(map(int, input().split()))
# board = defaultdict(list)
# temp_board = []
# check = [0] * h
# for i in range(n):
#     temp = int(input())
#     if i % 2 == 0:  # 아래
#         # for j in range(temp):
#         #     check[j] += 1
#         board['up'].append(temp)
#         temp_board.append(temp)
#     else:  # 위
#         # for j in range(-1, -1-temp, -1):
#         #     check[j] += 1
#         board['down'].append(temp)
#         temp_board.append(-1-temp)
# print(check,board,temp_board)

# min_num = float('inf')
# count = 0
# for i in check:
#     if i < min_num:
#         min_num = i
#         count = 1
#     elif i == min_num:
#         count += 1
# print(min_num, count)
