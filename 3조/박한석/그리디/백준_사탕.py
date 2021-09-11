# 백준 11256번 사탕
from sys import stdin
input = stdin.readline
t = int(input())
result = []
for i in range(t):
  j, n = map(int, input().split())
  arr = []
  for k in range(n):
    r, c = map(int, input().split())
    arr.append(r*c)
  arr.sort(reverse=True)
  count = 0
  l = 0
  while j > 0:
    j -= arr[l]
    l += 1
    count += 1
  result.append(count) 
for s in range(t):
  print(result[s])
