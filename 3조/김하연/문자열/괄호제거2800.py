import sys, copy
from itertools import combinations
f = sys.stdin.readline
ex = list(map(str, f().strip()))
s, pos, ans = [], [], set()

for i, v in enumerate(ex):
    if v == '(':
        s.append(i)
    if v == ')':
        t = s.pop()
        pos.append((t, i))

for i in range(1, len(pos)+1):
    comb = combinations(pos, i)
    for j in comb:
        temp = copy.deepcopy(ex)
        for s, e in j:
            temp[s] = ''
            temp[e] = ''
        ans.add(''.join(map(str, temp)))
for i in sorted(list(ans)):
    print(i)