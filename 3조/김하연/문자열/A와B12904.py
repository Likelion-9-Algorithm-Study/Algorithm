import sys
from collections import deque
f = sys.stdin.readline

s = f().strip()
t = deque(str(f().strip()))

while len(s) != len(t):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()

if s == ''.join(t):
    print(1)
else:
    print(0)

