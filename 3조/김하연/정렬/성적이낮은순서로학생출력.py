import sys
input = sys.stdin.readline
dict = {}
N = int(input())
for i in range(N):
    name, score = input().split()
    dict[name] = int(score)
result = sorted(list(dict.items()),key= lambda x: x[1])
for i in result:
    print(i[0], end=' ')