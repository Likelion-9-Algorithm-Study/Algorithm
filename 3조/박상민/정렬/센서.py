# https://www.acmicpc.net/problem/2212
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensors = sorted(list(map(int, input().split())))

diff = sorted([sensors[i]-sensors[i-1] for i in range(1, len(sensors))], reverse=True)
if n >= k:
    for _ in range(k-1):
        diff.pop(0)
else:
    print(0)
if n >= k:
    print(sum(diff))
