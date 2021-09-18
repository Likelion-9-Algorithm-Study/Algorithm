import sys
from itertools import combinations
f = sys.stdin.readline

l, s = map(int, f().split())
alpha = list(map(str, f().split()))
alpha.sort()
alpha = list(combinations(alpha, l))

for a in alpha:
    vow, cons, temp = 0, 0, ''
    for x in a:
        if x in ['a', 'e', 'i', 'o', 'u']:
            vow += 1
        else:
            cons += 1
        temp += x
    if vow >= 1 and cons >= 2:
        print(temp)
