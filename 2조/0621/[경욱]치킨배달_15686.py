import sys
from itertools import combinations
N, M = list(map(int, sys.stdin.readline().split()))
board = []
home = []
chicken = []
for i in range(N):
    temp_list = list(map(int, sys.stdin.readline().split()))
    for j in range(len(temp_list)):
        temp = temp_list[j]
        if temp == 2:
            chicken.append([i, j])
        elif temp == 1:
            home.append([i, j])
check_list = list(combinations(chicken, M))

result = float('inf')
for i in check_list:
    temp_sum = 0
    for j in home:
        distance = float('inf')
        for k in i:
            temp = abs(j[0]-k[0]) + abs(j[1]-k[1])
            if temp < distance:
                distance = temp
        temp_sum += distance
    if result > temp_sum:
        result = temp_sum
print(result)
