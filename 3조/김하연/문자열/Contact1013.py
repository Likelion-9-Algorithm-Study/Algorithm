import sys
import re

f = sys.stdin.readline

t = int(f())

def answer(string):
    p = re.compile('(100+1+|01)+')
    res = p.fullmatch(string)
    if res:
        return 'YES'
    else:
        return 'NO'


for _ in range(t):
    string = f().strip()
    print(answer(string))