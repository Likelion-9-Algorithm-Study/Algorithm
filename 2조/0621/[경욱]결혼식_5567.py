import sys
from collections import defaultdict
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
check = [False] * (n+1)
check[1] = True
graph = defaultdict(list)
for i in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)

result = 0
temp_list = []

for i in graph[1]:
    result += 1
    temp_list.append(i)
    check[i] = True

for i in temp_list:
    for j in graph[i]:
        if check[j] == False:
            result += 1
            check[j] = True
print(result)
