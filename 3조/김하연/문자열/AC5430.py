import sys
from collections import deque
f = sys.stdin.readline

T = int(f())

for _ in range(T):
    try:
        p = f().strip()
        n = int(f())
        x = f().strip()[1:-1].split(',')
        if x[0] == '': x = deque()
        else: x = deque(x)
        rev = False
        for i in p:
            if i == 'R':
                rev = not rev
            elif i == 'D':
                if rev: x.pop()
                else: x.popleft()
        if rev: x.reverse()
        print("[" + ",".join(x) + "]")

    except:
        print('error')



'''
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
'''
