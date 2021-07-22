import sys
input = sys.stdin.readline

N = int(input())
number = []
for i in range(N):
    number.append(int(input()))
number.sort(reverse=True)
for i in number: print(i)