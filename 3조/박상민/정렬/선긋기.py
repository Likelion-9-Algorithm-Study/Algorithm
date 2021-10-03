# https://www.acmicpc.net/problem/2170
import sys
input = sys.stdin.readline

n = int(input())
numlist = sorted((list(map(int, input().split())) for _ in range(n)))
leng = numlist[0][1] - numlist[0][0]
target = numlist[0][1]

for i in range(1, len(numlist)):
    if numlist[i][0] < target < numlist[i][1] or numlist[i][0] == target:
        leng += numlist[i][1] - target
        target = numlist[i][1]
    elif numlist[i][0] > target:
        leng += numlist[i][1] - numlist[i][0]
        target = numlist[i][1]

print(leng)
