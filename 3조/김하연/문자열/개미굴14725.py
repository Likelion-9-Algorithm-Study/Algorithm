import sys
input = sys.stdin.readline

N = int(input())
d = {}

for _ in range(N):
    ant = list(input().split())
    t = d
    for i in ant[1:]:
        if i not in t:
            t[i] = {}
        t = t[i]

def solution(t, i):
    keys = sorted(t.keys())
    for k in keys:
        print('--' * i + k)
        solution(t[k], i+1)

solution(d,0)

