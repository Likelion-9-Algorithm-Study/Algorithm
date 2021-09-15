import sys
from itertools import combinations
f = sys.stdin.readline

n, m = map(int, f().split())
city = [list(map(int, f().split())) for _ in range(n)]
house, chicken = [], []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])
comb = list(combinations(chicken, m))
result = sys.maxsize

for c in comb:
    temp_sum = 0
    for i, j in house:
        temp = sys.maxsize
        for x, y in c:
            temp = min(temp, abs(x-i) + abs(y-j))
        temp_sum += temp
    result = min(temp_sum, result)

print(result)
